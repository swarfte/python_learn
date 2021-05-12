'''
Author: Swarfte_Tou
Date: 2021-05-12 17:05:58
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-12 21:58:24
FilePath: \Python\python_learn\進階的\錯誤處理.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因
try:#*当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
    print("hello")
    #a = 10 / 0 
    #print(a) #*此時改為執行except部份
    print("你好")
except ZeroDivisionError as c :#*一個try內能含多個except對應不同的情況,像這個是除以0的錯誤
    print(c)
except : #*，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块
    print("出錯了")
else: #*当没有错误发生时，会自动执行else语句
    print("沒有錯誤")
finally:#*果有finally语句块，则执行finally语句块
    print("end")
    
    
# def foo(s):
#     return 10 / int(s)#*調用到這一步時會報錯

# def bar(s):
#     return foo(s) * 2

# def main():
#     bar('0')

# main()#*如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出


import logging  as log #*Python内置的logging模块可以让Python解释器来打印出错误堆栈,然后分析错误原因，同时，让程序继续执行下去 
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        log.exception(e) #*這一步會返回錯誤,並繼續執行程式,不會像一般的報錯那樣打斷程式

main()
print('END')

class FooError(ValueError):#*因为错误是class，我们自己编写的函数也可以抛出错误,可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误
    pass

def food(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)#*會把自定義的錯誤類型印出來
    return 10 / n

food('0')