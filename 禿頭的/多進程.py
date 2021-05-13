'''
Author: Swarfte_Tou
Date: 2021-05-13 17:17:25
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-13 22:18:06
FilePath: \Python\python_learn\禿頭的\多進程.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%在windows環境下,multiprocessing模块用作多进程,同時配搭os模組使用
import multiprocessing as mp
import os
import time 
import random as rd

#%啟動單個子進程
# def another(text):
#     print(f"測試內容:{text} ,進程ID:{os.getpid()} ")#*os.getpid用作獲取當前的進程ID
    
# if __name__ == '__main__':
#     print(f"目前的進程ID:{os.getpid()}")
#     T = mp.Process(target=another,args=("另一個進程",))#*使用Process方法實例化,target傳要子進程要跑的函數,args傳入對應的參數
#     T.start()#*執行子進程
#     T.join()#*等待子进程结束后再继续往下运行
#     print("進程結束")
    
# #%如果要启动大量的子进程，可以用进程池的方式批量创建子进程
# def time_check (text) :
#     print(f"進程:{text} ,進程ID:{os.getpid()} ")
#     start= time.time()#*記錄開始調用時的時間
#     time.sleep(rd.random()* 3)#*讓子進程進入休眼(待機)狀態
#     end = time.time()
#     print(f"進程:{text} ID :{os.getpid()} 一共運行了{end - start} 秒")
    
# if __name__ == '__main__':
#     print(f"目前的進程ID:{os.getpid()}")
#     RUN = mp.Pool(4)#*讓RUN變成Pool對像(註:Pool必須要大寫),這樣就能用RUN進行多線程工作,pool的默认大小是CPU的核数,若pool為4,則最多一次跑4個進程
#     [RUN.apply_async(time_check,args = (x,)) for x in range(5)]#*apply_async方法讓run執行多線程工作,第1個參數傳入要執行的函數,args為傳入的函數的參數
#     print("等待子進程運行")
#     RUN.close()
#     RUN.join()
#     print("全部進程階執行完成")

#%进程间通信
#%Python的multiprocessing模块提供了Queue、Pipes等多种方式来交换数据
import multiprocessing as mp
import os , time , random
def write(text) :
    name = os.getpid()
    print(f"進程ID:{name} 正在被調用寫入功能")
    L = ["ben","apple","banana"]
    for x in L :
        print(f"進程ID:{name} 寫入了 {x}")
        text.put(x)#*輸出數據至傳入的參數中
        time.sleep(random.random())

def read(text):
    name = os.getpid()
    print(f"進程ID:{name} 正在被調用讀取功能")
    while True:
        x = text.get(True)#*讀取取入的參數的內容
        print(f"讀取的內容:{x}")
        
if __name__ == '__main__':
    a = mp.Queue() #*# 创建一個Queue，并传给各个子进程,Queue可理由為一個線程"容器"
    b = mp.Process(target=write, args=(a,))#*B進程用作寫入
    c = mp.Process(target=read, args=(a,))#*C進程用作讀取
    b.start()
    c.start()
    b.join()#*等待B結束
    c.terminate() #* c进程里是死循环(while True)，无法等待其结束，只能强行终止: