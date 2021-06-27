def recall():
    string = ""#初始化
    while True:
        number = yield string #!通過yield把外部結果傳入string,同時也令用yield把string輸出,#赋值语句先计算= 右边，由于右边是 yield 语句，所以yield语句执行完以后，进入暂停，而赋值语句在下一次启动生成器的时候首先被执行
        if not number:#如果接收到0
            return #則結束
        print(f"recall get number is {number}")
        string = "recalling is ok"#*發送完ok之後便暂停,等待yield接受參數

def call(getter):
    getter.send(None)#*這個getter就是recall函數,把None值傳入yield那進行初始化,且在yield被中斷,等待賦值
    number = 0 #設定初始值
    while number < 10: #少於10的時候才執行
        number += 1
        print(f"calling number is {number}")
        get_number = getter.send(number)#*這裡把當前的number值傳入recall函數,此時recall函數的number被賦值為當前的number
        print(f"{get_number}")
    getter.close()#中斷協程
    
if __name__ == '__main__':
    r = recall()
    call(r)