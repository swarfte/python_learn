from flask import Flask, render_template, request, session, copy_current_request_context
from vsearch import search4letters
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in
from threading import Thread

app = Flask(__name__)
app.config['dbconfig'] = {
    'host': '127.0.0.1',
    'user': 'vsearch',
    'password': 'vsearchpasswd',
    'database': 'vsearchlogDB'
}


# @app.route('/')
# def hello() -> '302':  # 300-399範圍內的html狀態碼是重定向
#     return redirect('/entry')  # 用於重新定向

# 存放在vsearch.log中
# def log_request(req: 'flask_request', res: str, ) -> None:
#     with open("vsearch.log", "a") as log:
#         # print(req.form, file=log, end='|')  # 來源的<form>資料
#         # print(req.remote_addr, file=log, end='|')  # 來源的ip資料
#         # print(req.user_agent, file=log, end='|')  # 來源的用戶代理資料
#         # print(res, file=log, end='|')  # 回傳給來資的資料
#         print(req.form, req.remote_addr, req.user_agent, res, file=log, sep="|")  # sep參數用於多個輸出時的分隔符


# 存放在mysql vsearchlogDB中
# def log_request(req: 'flask_request', res: str) -> None:
#     dbconfig = {
#         'host': '127.0.0.1',
#         'user': 'vsearch',
#         'password': 'vsearchpasswd',
#         'database': 'vsearchlogDB'
#     }
#     conn = mysql.connector.connect(**dbconfig)
#     curses = conn.cursor()
#     _SQL = """insert into log
#             (phrase,letters,ip,browser_string,results)
#             values
#             (%s,%s,%s,%s,%s)"""
#     curses.execute(_SQL, (req.form['phrase'],
#                           req.form['letters'],
#                           req.remote_addr,
#                           req.user_agent.browser,
#                           res))
#     conn.commit()
#     curses.close()
#     conn.close()


@app.route('/search4', methods=["POST"])  # methods用於通訊的方法
def do_search() -> 'html':  # 提示回傳的內容是html
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """log details of the web request and the results"""
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
                         (phrase,letters,ip,browser_string,results)
                         values
                         (%s,%s,%s,%s,%s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res))

    phrase = request.form["phrase"]  # 獲取來源html中<form>標籤內name=phrase的<input>標籤內容
    letters = request.form["letters"]  # 獲取來源html中<form>標籤內name=letters的<input>標籤內容
    title = "Here are your results:"
    results = str(search4letters(phrase, letters))  # 把回傳的set類型轉換為str方便處理
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('***** Logging failed with this error:', str(err))

    return render_template('results.html',  # 返回一個網頁,此處使用results模版
                           the_title=title,  # 把python中的變量傳入模中對應的jinja2變量
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results
                           )


# 這時會依次匹配多個URL 如果找到其中一個匹配便會執行這個函數
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to search4letters on the web!")  # 同上


# @app.route('/viewlog')
# def view_the_log() -> 'html':
#     contents = []  # 創建一個大的列表裝入整理完的數據
#     with open("vsearch.log") as log:
#         for x in log:  # 讀取log中的每一行數據
#             contents.append([])  # 為每行數據創建一個列表
#             for y in x.split("|"):  # 以|符號分隔開每行的數據,放在對應的列
#                 contents[-1].append(escape(y))  # 對目前的符號進行轉義 並放入最後的行
#     print(contents)
#     titles = ('Form Data', 'Remote_addr', 'user_agent', 'Results')
#     return render_template('viewlog.html',
#                            the_title='View Log',
#                            the_row_titles=titles,
#                            the_data=contents
#                            )

@app.route('/viewlog')
def view_the_log() -> 'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase,letters,ip,browser_string,results
            from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
            titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
            return render_template('viewlog.html',
                                   the_title='View Log',
                                   the_row_titles=titles,
                                   the_data=contents
                                   )
    except ConnectionError as err:
        print('Is your database switched on? Error: ', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error: ', str(err))
    except SQLError as err:
        print('Is your query correct? Error: ', str(err))
    except Exception as err:
        print('Something went wrong: ', str(err))
    return 'Error'


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page 1'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'This is page 2'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'This is page 3'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


app.secret_key = 'YouWillNeverGuessMySecretKey'


@app.route('/logout')
def do_logout() -> str:
    del session['logged_in']
    return 'You are now logged out'


if __name__ == '__main__':
    app.run(debug=True)
