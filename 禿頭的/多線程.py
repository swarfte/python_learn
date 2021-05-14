'''
Author: Swarfte_Tou
Date: 2021-05-13 22:23:31
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-14 18:21:38
FilePath: \Python\python_learn\禿頭的\多線程.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%threading模組能在Python實現多線程的工作
import time
import threading as td
def hello(num):
    name = td.current_thread().name #*current_thread()函数返回当前线程的实例
    print(f"目前調用的線程名:{name} ")
    for x in range(num) : #*會輸出num次
        time.sleep(x)#*等待
        day = time.asctime( time.localtime(time.time()) )#*asctime用作格式化時間,localtime把時間轉換為目前時區
        print(f"線程 {name} 目前的時間:{day} ")
        
# print(f"目前正在運行 {td.current_thread().name} 線程 ")
# T1 = td.Thread(target=hello,name = "測試1",args =(5,))#*Thread函數用作創建另一條線程,target指定執行的函數,name指定該線程的名稱,如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
# T1.start()#*啟動該線程
# T1.join()#*等待線程結束
# print("全部線程已經執行完畢")

#%假如不為線程加鎖的話,有可能導致數據不同步
#%像下面這組代碼,不加鎖前輸出的結果有可能不為0,但加鎖後必為0(預期輸出)
money = 0
look = td.Lock() #*設置一個多線程的鎖
def play (num) :
    global money
    look.acquire()#*用acquire方法讓某一線程獲取鎖,有鎖的線程才能繼續執行代碼
    try :#*用try...finally来确保锁一定会被释放。
        name = td.current_thread().name
        for x in range(1,num) :
            money += x
            time.sleep(x / 500)
            money -= x
            print(f"線程 {name} 目前的存款:{money}")
    finally:
        look.release()#*release方法用作釋放鎖


T1 = td.Thread(target=play,args=(50,),name= "測試1")
T2 = td.Thread(target=play,args=(100,),name ="測試2")
D = td.Thread(target=hello,name = "檢測機" , args=(6,))
D.start()
T1.start()
T2.start()
D.join()
T1.join()
T2.join()
print(money)

