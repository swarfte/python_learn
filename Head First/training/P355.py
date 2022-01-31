# @app.route('/viewlog')
# def view_the_log() -> 'html':
#     with UseDatabase(app.config['dbconfig']) as cursor:
#         _SQL = """select phrase,letters,ip,browser_string,results
#         frmo log"""
#         cursor.execute(_SQL)
#         contents = cursor.fetchall()
#         titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
#         return render_template('viewlog.html',
#                                the_title='View Log',
#                                the_row_titles=titles,
#                                the_data=contents
