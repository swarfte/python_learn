'''
Author: Swarfte_Tou
Date: 2021-05-10 18:12:07
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-10 18:21:21
FilePath: \python\python_learn\進階的\filter.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%filter()函数用于过滤序列
def double (x) :
    return x % 2 == 0 #*由return得知這是一個用作篩選的函數
L =list(range(10))
C = filter(double,L)#*filter()把传入的函数依次作用于每个元素,然后根据返回值是True还是False决定保留还是丢弃该元素
print(C)#*filter函數翻回一個生成器
print(list(C))#*借助list生成結果

########################
#%這一般的方法實現
D = []
for x in L :
    if x % 2 == 0 :
        D.append(x)
print(D)#*結果和filter函數一樣