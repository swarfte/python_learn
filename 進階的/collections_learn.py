'''
Author: Swarfte_Tou
Date: 2021-05-17 22:51:17
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-17 23:39:23
FilePath: \Python\python_learn\進階的\collections.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%collections是Python内建的一个集合模块，提供了许多有用的集合类。
import collections as ct

#%namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
num = (10,5,7)#*表示一個點的二維座標
#!"pos"為point這個參數的對像
point = ct.namedtuple('pos', ['x', 'y',"z"])#*namedtuple方法用来创建一个自定义的tuple对象，并且规定了tuple元素的个数
a = point(num[0],num[1],num[2])
print(isinstance(a,point))
print(isinstance(a, tuple))#*Point对象是tuple的一种子类
print(a.x , a.y , a.z)

#%deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
b = ct.deque(range(10))#*deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
b.popleft()#*和pop一樣,只不過是彈出左手邊的元素
b.pop()
b.append(88)
b.appendleft(100)#*和append一樣,只不過是在左手邊加入元素
print(b)

#%defaultdict和dict一樣,但當defaultdict出錯時,會返回默認值
DD = ct.defaultdict(lambda: "不存在")#*傳入一個函數,這是出錯時翻回的默認值
DD["num"] = 132
print(DD["abc"])
print(DD["num"])

#%使用dict时,如果要保持Key的顺序，可以用OrderedDict
CC = ct.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(list(CC.values()))#*用keys的話會反回對應的key

#%注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
oo = ct.OrderedDict()
oo["c"] = 1
oo["f"] = 2
oo["a"] = 3
print(list(oo.keys()))#*用values則返回對應的數值

#%Counter是一个简单的计数器，例如，统计字符出现的个数
KK = ct.Counter()#*創建一個計數器
for x in "i go to school by bus" :
    KK[x] += 1
print(KK)#*連空白字符也會統計