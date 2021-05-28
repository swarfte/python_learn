'''
Author: Swarfte_Tou
Date: 2021-05-27 07:51:03
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-28 21:26:57
FilePath: \Python\python_learn\進階的\contextlib.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
import time

# #%利用__enter__和__exit__實現with的方法
# class test(object) :
#     def __init__(self,name):
#         self.name = name
#         self.time = 0
    
#     def __enter__(self):#*當with開始的時候調用
#         self.time = time.time()
#         print("開始調用")
#         return self #!重要,當with調用時,用作翻回自身,不然該函數為nonetype
    
#     def __exit__(self,exc_type, exc_value, traceback) :#*當with結束的時候調用,self,exc_type, exc_value, traceback要作檢差狀態
#         if exc_type :#*類型出錯
#             print("出現了錯誤")
#         else:
#             self.time = time.time() - self.time
#             print(f"花費了{self.time}秒")
    
#     def hello(self):
#         print(f"你好,{self.name}")
#         print(f"由1到100的偶數總和為:{sum([x for x in range(101) if x % 2 == 0])}")

# with test("ben") as T :#*可以像開文件一樣直接用with
#     T.hello()        
    
#%Python的标准库contextlib提供了更简单的写法
import contextlib as c
class test_user(object):#*利用contextlib改寫
    def __init__(self,name) :
        self.name = name
        self.time = 0
    
    def hello(self):
        print(f"你好,{self.name}博士")
        print(f"由1到1000的奇數總和為:{sum([x for x in range(1001) if x % 2 != 0])}")

#@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
@c.contextmanager #*利用contextlib的contextmanager實現with的功能並省略__enter__和__exit__
def log (user_name):#&調用的時候便用這個函數名取代物件
    use = time.time()
    print("開始調用")
    T = test_user(user_name)#*把接收的函數傳入test物件
    yield T #!這步很重要,在調用log函數時,會先執行 yield 前的代碼,當進入yiled時,會把指定的函數運行完才會繼續執行剩下的代碼
    use = time.time() - use #*所以這裡時間便是整個物件跑完函數(hello)的時間
    print(f"花費了:{use}秒")

# with log("JOJO") as L :
#     L.hello()
    
#%我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
import datetime as dt

@c.contextmanager
def call(name) :
    print(f"建議{name}不要睡死")
    print("目前時間:{dt.datetime.now()}")
    yield #*這裡的yield用作分隔兩部份,yield前的代碼會在with 的時候馬上調用,等with內的代碼執行完後,才繼續執行yield後的代碼
    print(f"{name}起床了")
    print(f"起床時間:{dt.datetime.now()}")

# with call("ben"):#*會自動執行
#     print("還在嗎")

import urllib.request as ul
#%用closing()来把该对象变为上下文对象,前提是該對像要有close屬性
# with c.closing(ul.urlopen('https://www.python.org')) as test :
#     for x in test :
#         print(x)
#%closing()的原理以下:
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
