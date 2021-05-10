'''
Author: Swarfte_Tou
Date: 2021-05-10 22:57:02
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-10 23:23:11
FilePath: \python\python_learn\禿頭的\對像進階.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%__slots__用作限制实例的属性,但__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class people(object):
    __slots__ = ("name","age")#*此時該對像的實例只能新增"name"和"age"的屬性(self.name和self.age)
C = people()
C.name = "ben"
print(C.name)
try :
    C.money = 900#*限制"名單"中沒有money這個屬性,所以會報錯
except :
    print("不行")
    
#@property装饰器是负责把一个方法变成属性调用
class admin () :
    
    @property
    def time(self):#*把一个getter方法(獲取方法)尸变成属性，只需要加上@property就可以了
        return self.__time 

    @time.setter #*把一个setter方法变成属性赋值,用作設置__time屬性的裝飾器
    def time(self,value) :
        self.__time = value

S = admin()
S.time = 80 #*初始化屬性
print(S.time)