'''
Author: Swarfte_Tou
Date: 2021-05-09 17:41:56
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 18:34:29
FilePath: \python\python_learn\generator.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
# #创建一个generator(生成器)，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
# g = (x for x in range(10))
# #print (g)#%反回生成器
# print(next(g))#*生成第一個元素
# print(next(g))#*生成第二個元素
# print(list(g))#%生成一個list [2,3,4,5,6,7,8,9],因為頭2個元素比next
# print(list(g))#*沒有元素
# z = (x for x in range(20))
# for x in z:#*使用for把每個元素都拋出來
#     print(x)

# def double (x):
#     j = x ** 2
#     a = x ** x
#     while j <= a:
#         #*yield為生成器的關鍵字
#         yield j #%此時函式變為了一個生成器
#         j *= j
#     #%該函式回傳yield 參數的值(如果符合條件)
# b =double(5)
# print(b)#*B為以4為參數的double函式的生成器
# print(list(b))#*a的值為3125,第一次的j為25,第2次的J為625,第3次為390625,第3次時j> a ,則只輸出頭2次結果

#print(sum([x for x in (y for y in (z for z in range(10))if y % 2 == 0 ) if x % 3 == 0]))#*列表推導式和生成器能一起用
