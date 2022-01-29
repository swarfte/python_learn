from flask import Flask, render_template, request, redirect
from vsearch import search4letters

app = Flask(__name__)


# @app.route('/')
# def hello() -> '302':  # 300-399範圍內的html狀態碼是重定向
#     return redirect('/entry')  # 用於重新定向


@app.route('/search4', methods=["POST"])  # methods用於通訊的方法
def do_search() -> 'html':  # 提示回傳的內容是html
    phrase = request.form["phrase"]  # 獲取來源html中<form>標籤內name=phrase的<input>標籤內容
    letters = request.form["letters"]  # 獲取來源html中<form>標籤內name=letters的<input>標籤內容
    ### 最大行數:3行
    title = "Here are your results:"
    results = str(search4letters(phrase, letters))  # 把回傳的set類型轉換為str方便處理
    return render_template('results.html',  # 返回一個網頁,此處使用results模版
                           the_title=title,  # 把python中的變量傳入模中對應的jinja2變量
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results
                           )
    ###


# 這時會依次匹配多個URL 如果找到其中一個匹配便會執行這個函數
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to search4letters on the web!")  # 同上


app.run(debug=True)
