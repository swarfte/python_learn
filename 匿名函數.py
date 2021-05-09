'''
Author: Swarfte_Tou
Date: 2021-05-09 19:14:54
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 19:20:19
FilePath: \python\python_learn\匿名函數.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#*关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
#此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
S = lambda x : x ** 2#*返回X的平方的值
print(S(2))
#同样，也可以把匿名函数作为返回值返回
def AaddB (a,b) :
    return lambda : a + b #*此時的函數回傳一個函數,和返回函數同理,需要再次使用該發數才能獲得對應的值
print(AaddB (10,25)())
