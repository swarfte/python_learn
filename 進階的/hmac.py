'''
Author: Swarfte_Tou
Date: 2021-05-21 23:15:50
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-21 23:21:21
FilePath: \1A\Python\python_learn\進階的\hmac.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%通过哈希算法，我们可以验证一段数据是否有效，方法就是对比该数据的哈希值
import hmac as h
#%需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
message = b"JOJO"#*原始資料
salt = b"2021"#*加鹽

#%需要准备待计算的原始消息message，随机key，哈希算法(disgestmod)
secret = h.new(salt,message,digestmod="MD5")#*用哈希算法加密,這裡採用MD5
print(secret.hexdigest())#*輸出結果
