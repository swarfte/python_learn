'''
Author: Swarfte_Tou
Date: 2021-05-21 23:26:37
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-21 23:47:21
FilePath: \Python\python_learn\進階的\itertools.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
import itertools as it

#%itertools提供了非常有用的用于操作迭代对象的函数。
def ct () :
    t1 = it.count(1)#*count()会创建一个无限的迭代器
    for x in t1 :
        if x < 100 :
            print(x)
        else:
            break#*需要手動停止

def cy () :
    run = 0
    t2 = it.cycle("Swarfte")#*cycle()会把传入的一个序列(str,list等可迭代的類型)无限重复下去
    for x in t2 :#*无限序列只有在for迭代时才会无限地迭代下去
        if run < 100 :
            print(x)
            run += 1
        else:
            break

def rp () :
    t3 = it.repeat("JOJO",3)#*repeat會不斷重覆傳入的元素,傳入參數可以指定重覆的次數
    for x in t3 :
        print(x)

def tw() :
    t4 = it.count(1)
    #%通过takewhile()等函数根据条件判断来截取出一个有限的序列
    num =it.takewhile(lambda x :x < 20,t4)#*利用lambda函式作篩選條件
    print(list(num))#*利用list的方式迭代輸出

def ch ():
    for x in it.chain("Swarfte","JOJO"):#*通過chain方式把兩組迭代对象串联起来
        print(x)#*然後輸出全部可迭代的內容

def gp():
    for x,y in it.groupby("CcCCSsSQeWFFfFFFXxXC", lambda x: x.upper()):#*groupby()把迭代器中相邻的重复元素挑出来放在一起,可傳入參數調整字符串
        print(x,list(y))#*X表示開頭,Y用作表示重覆的次數

if __name__ == "__main__" :
    #ct()
    #cy()
    #rp()
    #tw()
    #ch()
    gp()