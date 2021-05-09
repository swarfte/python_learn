'''
Author: Swarfte_Tou
Date: 2021-05-09 21:06:57
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 22:20:51
FilePath: \python\python_learn\基礎的\創建函數.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
def my_abs(x):#*像這樣
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-5))
    
#%定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass
print(nop())#*沒有結果

def pows(x):#*当我们调用pows函数时，必须传入有且仅有的一个参数x
    return x * x

def power(x, n=2):#*把第二个参数n的默认值设定为2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))#*相当于调用power(5, 2)

def calc(*numbers):#*在参数前面加了一个*号即表示可傳入無限多個參數
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#%关键字参数(**變量)允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):#*此處kw為關鍵字参数,在调用该函数时，可以只传入必选参数
    print('name:', name, 'age:', age, 'other:', kw)
    
#%如果要限制关键字参数的名字，就可以用命名关键字参数
def person(name, age, *, city, job):#*命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
    print(name, age, city, job)
#