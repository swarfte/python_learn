'''
Author: Swarfte_Tou
Date: 2021-05-09 20:04:42
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 20:29:22
FilePath: \python\python_learn\字典.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#*字典使用键-值（key-value）存储
#!dict(字典)的key(鍵)必须是不可变对象
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])#%d字典中"michael"對應的值
d['Adam'] = 67 #*在d字典中加入對應的值
print(d['Adam'])
d.pop('Bob')#*刪除d字典中"bob"鍵和對應的值
print(d)

N = ("ben","jojo","yoyo","Lok","pig")
DT = {}
for x in range(5) :
    DT[str(x)] = N[x]#*通過for的形式創建字典
print(DT)

#%或者利用字典推導式
S = {x: y for y, x in enumerate(N)}#*enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
print(S)