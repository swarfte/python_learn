import  socket as sk
#%使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
s = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)#*創建一個端口,UDP使用的是SOCK_DGRAM
ip = "127.0.0.1"
port = 9999
s.bind((ip,port))
print("監聽 UDP 9999 端口中")
while True :
    data,addr = s.recvfrom(1024)#*一次接收最大的資料數量
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
