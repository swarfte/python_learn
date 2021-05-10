'''
Author: Swarfte_Tou
Date: 2021-05-10 21:32:01
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-10 22:53:31
FilePath: \python\python_learn\進階的\對像.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%在Python中，定义类是通过class关键字,()用作繼承其他類別,object类是所有类最终都会继承的类。 #重要(class可以解為物件/對像/類)
class people (object) :#*名為people的對像,繼續object類
    def __init__(self, name, money,gender):#*__init__用作把屬性綁定(也可理解為預設屬性)
        self.name = name #*一般變量名前加self
        self.money = money
        self.__gender = gender #*變量名前加__表示該變量為私有變量,即不能被外部詢問
    
    def say(self) :#*對像的方法需要先放入self,再跟其他變量,__init__同理 
        print(f"{self.name},你好")
        
    def get_gender (self):#*外部獲得__gender這個私有變量的方法
        return self.__gender
    
a = people("ben",800,"male")#*a為people對像的實例 ##類的其中一個特點:封裝 每個實例都有不同的數據
print(a)#*返回的是實例化後的people
print(a.name)#*輸出a對像中name的屬性的值
print(a.say())#*輸入a對像中的方法(say),調用對像的方法時需要要括號
try :
    print(a.__gender)#*會報錯
except :
    print("找不到")

#%当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类，而被继承的class称为基类、父类或超类
class student(people) :#*people是基類,student是子類,student繼承了people類 #類的其中一個特點:繼承
    def listen (self) :#*可以对子类增加一些方法,只有子類特有
        print(f"{self.name}睡死了")
    def say (self) :#*当子类和父类都存在相同的方法时,子类會覆盖了父类的方法 #類的另一個特點:多态
        print(f"我破產了,只剩{self.money}元")
        
C = student("jojo",900,"female")
print(C.name)#*student的實孩對像直接繼承了people的全部屬性和方法
print(C.listen())

def speak (func):
    func.say()
speak(a)#*這是多态的好处,只要實例物件具有該函數的方法,就能調用
speak(C)#*雖然結果和a不同,但事實上是同一種方法,只是student復蓋了原先的寫法

#%利用isinstance()函數判斷子類和父類
print(isinstance(a,people))#*a是people的實例,True
print(isinstance(C,student))#*C是student的實例,True
print(isinstance(C,people))#*C是student的實例,student又是people的子類,True
print(isinstance(a,student))#*a是people的實例,但people不是student的子類,所以False

#%python中萬物皆對像,那麼物件一般會自帶各種變量
D = "abcde"
print(len(D) == D.__len__())#*由輸出True得出是相等的

#%在實例物件中,hasattr()用來檢測實例物件是否具有某種屬性 (可以看成 has attr)
print(hasattr(C,"name"))#*檢測C是否有"name"(self.name)這個屬性

#%在實例物件中,setattr()用作為實例物件設置一個變量(可以看成 set attr)
print(hasattr(C,"sleep_time"))#*沒有則輸出False
setattr(C,"sleep_time",8)#*為C實例增加一個屬性sleep_time,並設置為8
print(hasattr(C,"sleep_time"))#*此時屬性存在,則為True

#%在實例物件中,getattr()用作獲取實例物年中的屬性(前提該屬性存在,不然會報錯) (可以看成 get attr)
print(getattr(C,"sleep_time"))
print(getattr(C,"die","no"))#*也可以入加默認值,但找不到該屬性的值時返回默認值


