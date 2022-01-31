def log_request(req: 'flask_request', res: str) -> None:
    import mysql.connector
    dbconfig = {
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': 'vsearchpasswd',
        'database': 'vsearchlogDB'
    }
    conn = mysql.connector.connect(**dbconfig)
    curses = conn.cursor()
    _SQL = """insert into log
            (phrase,letters,ip,browser_string,result)
            values
            (%s,%s,%s,%s,%s)"""
    curses.execute(_SQL,(req.form['phrase'],
                         req.form['letters'],
                         req.remote_addr,
                         req.user_agent.browser,
                         res))
    conn.commit()
    _SQL = """select * form log"""
    curses.execute(_SQL)
    for row in curses.fetchall():
        print(row)
    curses.close()
    conn.close()
