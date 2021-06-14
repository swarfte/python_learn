import socket as sk
import threading
import time
s = sk.socket(sk.AF_INET,sk.SOCK_STREAM)#*创建一个基于IPv4和TCP协议的Socket
ip = "127.0.0.1"
port = 9999
s.bind((ip,port))#*創建一個端口用作监听
s.listen(5)#*调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
print("正在等待連接")

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')#*向用戶端發出信息
    while True:
        data = sock.recv(1024)#*最大接收資料量
        time.sleep(1)#*等待1秒
        if not data or data.decode('utf-8') == 'exit':#*接收到結束指令時
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))#*要轉碼
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock,addr = s.accept()#*接受一个新连接
    t = threading.Thread(target=tcplink, args=(sock, addr))#*接收到連接時執行tcplink這個函數
    t.start()
