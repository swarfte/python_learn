from email.mime.text import MIMEText
said = input("信息內容:")
msg = MIMEText(said,"plain","utf-8")#*打包成email的信息
user = input("使用者名稱:")
password = input("密碼:")
get = input("收信人:")
stmp_server = "smtp.gmail.com"

import smtplib as sp
server = sp.SMTP(stmp_server,587)#* gamil的端口是587
server.set_debuglevel(1)
server.login(user,password)#* 登入伺服器
server.sendmail(user,[get],msg.as_string())#*發信息到指定的位置
server.quit()#*結束通訊
