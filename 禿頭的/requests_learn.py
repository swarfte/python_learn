import requests as rq
#%requests一个Python第三方库，处理URL资源特别方便
url = rq.get("https://www.louhau.edu.mo/www/")
print(f"網站的狀態 : {url.status_code}")


