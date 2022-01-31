import mysql.connector  # 和mysql數據庫交互的數據庫驅動程式


def connect():
    config = {  # 用於連接mysql的4個必要資料
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': 'vsearchpasswd',
        'database': 'vsearchlogDB'
    }
    # **config 代表傳入一個參數字典,會把字典中的鍵/值 拆成獨立的參數傳入 並把字典中對應的值用參數賦值的形式傳入
    connection = mysql.connector.connect(**config)  # 與mysql中對應的庫進行連接
    curses = connection.cursor()  # 獲取該數據庫的遊標(用於操作該數據庫)
    #準備使用的SQL語句, % s為佔位符
    _SQL = """insert into log
            (phrase,letters,ip,browser_string,results)
            values
            (%s,%s,%s,%s,%s)"""  # 在log表中插入資料

    curses.execute(_SQL,
                   ('galaxy', 'xyz', '127.0.0.1', 'Opera', "{'x','y'}"))  # 需要兩個參數 第一個參數為要執行的sql語句 第二個參數為要SQL語句中的佔位符參數
    connection.commit()  # 對緩存中的資料進行強制寫入
    _SQL = """select * from log"""  # 獲取log表中的全部行
    curses.execute(_SQL)
    for row in curses.fetchall():  # 獲取遊標中的全部資料
        print(row)
    curses.close()  # 關閉遊標
    connection.close()  # 關閉和數據庫的連接


if __name__ == '__main__':
    connect()
