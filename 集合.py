'''
Author: Swarfte_Tou
Date: 2021-05-09 20:09:28
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 20:12:11
FilePath: \python\python_learn\集合.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)
s.add(4)#*通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
print(s)
s.remove(4)
print(s)#*通过remove(key)方法可以删除元素
#%两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)#*s1和s2的交集
print(s1 | s2)#*s1和s2的並集