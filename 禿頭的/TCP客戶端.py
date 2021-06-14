import socket as sk
#%通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可
#%客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号
s = sk.socket(sk.AF_INET,sk.SOCK_STREAM)#*建立一個socket,TCP使用的是SOCK_STREAM
url = "www.sina.com.cn"
port = 80
s.connect((url,port))#*用作用連接伺服器,用元祖表示網
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')#*要求返回首頁的資料
get = []
while True:
    d = s.recv(1024)# 每次最多接收1k字节
    if d :#*收到資料
        get.append(d)#*緩存一下
    else:
        break#*接收完則停止
date = b"".join(get)
s.close()
header,html = date.split(b'\r\n\r\n', 1)#*讀取資料
print(header.decode('utf8'))#*轉碼
with open("test.html","wb") as f:
    f.write(html)