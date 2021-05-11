'''
Author: Swarfte_Tou
Date: 2021-05-10 22:57:02
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-11 18:56:50
FilePath: \Python\python_learn\禿頭的\對像進階.py
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

#%PYTHON有多重繼承的方法
class Animal(object):#*最核心的類
    pass

# %大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# %各种动物:
class Bat(Mammal):
    pass

class Parrot(Bird):
    pass
class Runnable(object):#*新的分支
    def run(self):
        print('Running...')

class Flyable(object):#*新的分支
    def fly(self):
        print('Flying...')

#%新的類/物件能夠同時繼承多個類,這樣就能一次獲得多種屬性/方法
class Dog(Mammal, Runnable):#*像這樣一次繼承多種類,像狗這個對像,他既是哺乳动物類,同時又是運動的類型
    pass

#%另一方面,python支援定制類,即自定義函數版調用時的回傳
class people(object) :
    def __init__(self,name,old):
        self.old = old
        self.name = name
        self.save = self.old
        
    def __str__(self):#*當實例的對像被print()函數調用時,會回傳這個結果(__str__()返回用户看到的字符串)
        return f"傳入的名稱是{self.name}"
    __repr__ = __str__#*懶人寫法,__repr__()返回程序开发者看到的字符串,__repr__()是为调试服务的
    
    def __iter__(self):#*一个类想被用于for ... in循环,类似list或tuple,就必须实现一个__iter__()方法
        return self #*实例本身就是迭代对象，故返回自己
    
    def __next__(self):#*for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
        self.old += 1#*每次被調用時使自身加入
        if self.old >= len(self.name) ** 2 :#*當old>輸入的名稱的長度平方時會退出循環
            raise StopIteration()#*拋出StopIteration错误用來停止for ... in 的循環
        return self.old #*被next()函數調用時回傳的值
    
    def __getitem__(self,x) :#*__getitem__()方法讓對像能像list那樣按照下标取出元素
        a = self.save
        for i in range(x) :
            a += 1
        return a
    
    def __getattr__(self, attr):#*當調用不存在的屬性時,會調用以下函數
        if attr=='age': #*當調用對像的"age"屬性時
            return self.old #*回傳old的值
        raise AttributeError ("不存在這個屬性") #*調用非特定不存在屬性時,會拋出自定義的報錯信息
        
    def __call__(self):#*定义一个__call__()方法，就可以直接对实例进行调用
        print(f"正在調用__call__方法")
    
A = people("benjamin",18)
print(A)
for i in A :#*加了__iter__和__next__方法後便能利用for ... in 獲取對像的值
    print(i)
print(A[3])#*加了__getitem__方法後便能像list一樣利用下標獲得值
print(A.age)#&這個值是經過for循環加算後的值
#print(A.ccc)#*會出現錯誤,並輸出自定義的報錯信息
A()#*不用print而是直接調用

#%Enum类用作枚举,定义一个class类型，然后，每个常量都是class的一个唯一实例
from enum import Enum 

year = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))#*以Month為一個類,後面的元祖/列表的元素為該類的唯一實例
#%访问这些枚举类型可以有若干种方法
print(year.Jan)#*獲得一月
print(year["Feb"])#*獲得2月
print(year(3))#*獲得3月

#%type()函数既可以查看一个类型或变量的类型,，又可以创建出新的类型
def use(self, name='world'): #*先定义模版函數
    print('Hello, %s.' % name)
    
#%要创建一个class对象，type()函数依次传入3个参数
SAY = type('Hello', (object,), dict(sayhello=use))#*第1個參數是class的名称,第2個參數是继承的父类集合(需要用tuple形式表示),第3個參數是class的方法名称与函数绑定
test = SAY()#*用test把SAY對像實例
test.sayhello()#*調用sayhello方法

#&python的metaclass是一種特殊的魔法方法
#%先定义metaclass，就可以创建类，最后创建实例
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value) #*為用這個metaclass方法生成的類定義初始的屬性add
        return type.__new__(cls, name, bases, attrs)#*回傳經過自定義的對像

class MyList(list, metaclass=ListMetaclass):#*指定用ListMetaclass模版建立這個類
    pass

#%传入关键字参数metaclass时,了，它指示Python解释器在创建類時,要通过ListMetaclass.__new__()来创建,因此我們能在__nwe__()中加了新的方法等
C = MyList()
C.add(2)#*因為C這個實例是用自定義的ListMetaclass所建立的類生成的,所以實例自帶add這個屬性
print(C)#*剛才加了2,所以輸出2
#!然而一般情況下都是在實例C後再增加該屬性比較方便