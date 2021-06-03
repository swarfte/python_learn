
#%urllib提供了一系列用于操作URL的功能。

import urllib.request as ur

#%urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
def get_url():
    with ur.urlopen("https://www.louhau.edu.mo/www/") as LH :#*連線至特定網站,LH為網站返回的資料
        date = LH.read()#*讀取回傳的網站
        print(f"網站的狀態 : {LH.status} -> {LH.reason}")
        for x , y in LH.getheaders() :#*獲取監聽的網站的資料
            print(f"{x} : {y}")#*以類字典的形式輸出獲得的各種資料
        print("---------------------------------------")
    
#%如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
def send_get():
    url = "https://www.op.gg/champion/sett/statistics/top"#*要連線的網頁
    agent = 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'#*假裝自己是Iphone 6
    with ur.urlopen(url) as opgg :
        print("狀態 : {opgg.status} -> {opgg.reason}")
        for x , y in opgg.getheaders():
            print(f"{x} : {y}")


#%POST用作向伺服器發送資料,模擬登入/點擊的情景,如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
def send_post():
    pass


if __name__ == '__main__':
    #get_url()
    #send_get()
    pass

