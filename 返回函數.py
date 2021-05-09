'''
Author: Swarfte_Tou
Date: 2021-05-09 18:34:44
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 19:12:48
FilePath: \python\python_learn\返回函數.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# def sum (*a):#*基本的函數
#     ans = 0
#     for x in a :
#         ans += x
#     return ans
# print(sum(1,2,3))

def lazy_sum(a):#*複合函數
    def sum ():
        ans = 0
        for x in a:
            ans += x
        return ans
    return sum #*回傳一個函數
number = [1,2,3,4]
S = lazy_sum(number)
print(S)#*此時回傳的是一個函數
#!有兩種方法可以獲得結果
print(S())#*方法一,先把函數傳進一個變量,而且使用該函數
print(lazy_sum(number)())#*方法二,在該函數後跟()
