import requests as rq
#%requests一个Python第三方库，处理URL资源特别方便
url = rq.get("https://www.louhau.edu.mo/www/")
print(f"網站的狀態 : {url.status_code}")
#print(url.text)#*獲取網站的代碼
#%带参数的URL，可以传入一个dict作为params参数,這樣params會把對應的值填充
search = rq.get("https://www.google.com/webhp?hl=zh-TW&sa=X&ved=0ahUKEwjHwJHJv_rwAhUSA4gKHUPDCCoQPAgI",params = {"q" : "Swarfte"})
print(search.text)
