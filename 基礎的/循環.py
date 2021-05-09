'''
Author: Swarfte_Tou
Date: 2021-05-09 19:43:31
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 21:53:15
FilePath: \python\python_learn\循環.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
L = [1,2,3]
for x in L : #*創建一個變量x,依次由L中提取元素
    print(x)
print([x for x in L])#*各種推導式也循環的一種
    
LO = [["x",1],["y",2],["z",3]]
for x,y in LO :#*能支援多個變量
    print(x,y)

#*第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#*在循环中，break语句可以提前退出循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#*在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
    
#