'''
Author: Swarfte_Tou
Date: 2021-05-09 19:30:11
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 22:20:35
FilePath: \python\python_learn\基礎的\列表和元祖.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#*list是Python内置的一种数据类型
#*list是一种有序的集合，可以随时添加和删除其中的元素。
#%numpy的陣列比原生的list實用^_^
L =[1,2,3,4]
print(L)
N = L[1]#*獲得列表L的第2個元素,(素引由0數起)
print(N)
M = L[-2]#*獲得列表倒數第2個元素
print(M)
L.append(8)#*在列表的最後加入8 ,(順序加入)
print(L)
L.insert(1,1.5)#*在第2個(素引第1個)位置插入1.5
print(L)
L.pop(3)#*刪除列表中第4個元素
print(L)
L[1] = 11#*把列表中第11個元素替換為11
print(L)
B = [1,1.3,"name"]#*列表可以由不同的數據類型組成
lo = len(L)#*求出L列表的長度
print(lo)
C = [[1,2],[3,4]]#*列表也能多維的
print(C)

#%元組和列表有9成相似
#*但是tuple一旦初始化就不能修改
A = ("name","bne")
print(A)
C = tuple("J")#*要定义一个只有1个元素的tuple的方法
#*可变的"tuple"
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)#*雖然內容變了,但是第1層(元祖那層)沒有變化,變化的是list那層的元素
#