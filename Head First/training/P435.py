# @app.route('/search4', methods=["POST"])  # methods用於通訊的方法
# def do_search() -> 'html':  # 提示回傳的內容是html
#     phrase = request.form["phrase"]  # 獲取來源html中<form>標籤內name=phrase的<input>標籤內容
#     letters = request.form["letters"]  # 獲取來源html中<form>標籤內name=letters的<input>標籤內容
#     title = "Here are your results:"
#     results = str(search4letters(phrase, letters))  # 把回傳的set類型轉換為str方便處理
#     try:
#         log_request(request,results)
#     except Exception as err :
#         print('***** Logging failed with this error:',str(err))
#
#     return render_template('results.html',  # 返回一個網頁,此處使用results模版
#                            the_title=title,  # 把python中的變量傳入模中對應的jinja2變量
#                            the_phrase=phrase,
#                            the_letters=letters,
#                            the_results=results
#                            )