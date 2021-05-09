'''
Author: Swarfte_Tou
Date: 2021-05-09 21:19:15
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 21:23:11
FilePath: \python\python_learn\遞歸函數.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%遞歸函數的特點是會在特點的情況下return自己
#!递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))#& fact(5) --> 5*fact(4) --> 5*4*3*fact(2) --> 5*4*3*2*fact(1) -->5*4*3*2*1
#

