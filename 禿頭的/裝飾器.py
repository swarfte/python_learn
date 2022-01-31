# # '''
# # Author: Swarfte_Tou
# # Date: 2021-05-10 19:01:48
# # LastEditors: Swarfte_Tou
# # LastEditTime: 2021-05-10 19:42:48
# # FilePath: \python\python_learn\禿頭的\裝飾器.py
# # FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
# # GithubName: Swarfte
# # GithubURL: https://github.com/swarfte/Swarfte.git
# # GithubLazy: git init git commit -m git push -u
# # '''
# # #%裝飾器算是語法糖的一種
# # #%函数是一个对象,同時函数对象可以被赋值给变量,所以能通过变量调用该函数
# # import datetime as DT

# # def now_time () :#*一個普通的函數
# #     print(DT.datetime.now())#*輸出現在的時間
# # #&注意 T = now_time 是沒有括號的,因為要把now_time()函數賦值給T,讓T具有和now_time()函數相同的功能
# # T = now_time#*把函數對像賦值給變量 
# # # T() #*通过变量调用该函数
# # #&上面的例子說明了函數的特性


# # # #%首先要知道的是函數對像有一個屬性__name__,這個屬性記錄了屬性的名稱
# # # print(now_time.__name__)#*now_time函數的名字當然是now_time
# # # print(T.__name__)#*因為把函數對像賦值給變量,所以變量T的__name__和該函數一樣

# # #%裝飾器的其中一種用法是用作增強原有函數的功能
# # #%例如令函數在調用前輸出"正在調用一個函數"函數,同時不修改原函數,这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# # #&本质上，裝飾器就是一个返回函数的高阶函数
# # def log(func):#*這個函數用作在函數被調用前輸出"正在調用一個函數"
# #     def see():
# #         print("正在調用一個函數")
# #         return func()#*回傳並執行輸入的函數
# #     return see #*當log()被調用時,回傳see()函數,此時see便print出句子

# # #%建立一個新的函數測試裝飾器的效果,裝飾器的語法是@ + 函數名,@要交在函数的定义处
# # @log #*這樣的寫法相當於 this_time = log(this_time)
# # def this_time() :
# #     print(DT.datetime.now())#*和剛才的函數一樣
# # #this_time()
# # #&說明:由于log()是一个裝飾器,調用時會返回一个函数,此時原来的函数仍然存在,只是现在同名的变量被賦值為新的函数,所以當我們執行this_time()時,事實上是執行了log(this_time)

# # #%裝飾器也能用多層結構
# # def status (text) :#*這個裝飾器能輸出調用函數時的時間,以及被調用函數的名稱
# #     def time (func) :
# #         time = DT.datetime.now()
# #         def say() :
# #             print(f"{text} 現在的時間為{time} ,被調用的函數為{func.__name__} ")
# #             return func()
# #         return say
# #     return time

# # @status("狀態:")#*text變量在這輸入
# # def hello () :
# #     print("hello world")

# # hello()

# #------------------------------------------------------------------------------------

# 定義裝飾器
# def 裝飾器名稱(回呼函式名稱):
#   def 內部裝飾器名稱():
#       #裝飾器內部的程式碼
#       回呼函式名稱
#   return 內部裝飾器名稱

# def myDeco(callback):
#     def run():
#         print("裝飾器中的程式碼")
#         callback()
#     return run

# def checkTime(callback):
#     import datetime
#     def run():
#         start = datetime.datetime.now()
#         callback()
#         end = datetime.datetime.now() - start
#         print(f"花費了{end}時間")
#     return run

# @myDeco
# def test():
#     print("普通程式的程式碼")
# # test()

# @checkTime
# def testing():
#     print("測試運行中")

# testing()

# 定義一個裝飾器,計算1+2+...+50的總和
def calculate(callback):
    def run():
        # 裝飾器想要執行的程式碼
        result = 0
        for x in range(51):
            result += x
        # 把計算的結果傳入被裝飾的普通裝飾中
        callback(result)

    return run


# 使用裝飾器
@calculate
def show(n):
    print("計算結果是 ", n)


show()


@calculate
def englishShow(n):
    print("the calculate answer is ", n)


englishShow()
