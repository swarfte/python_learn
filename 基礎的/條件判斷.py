'''
Author: Swarfte_Tou
Date: 2021-05-09 19:40:54
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 22:20:43
FilePath: \python\python_learn\基礎的\條件判斷.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
age = 20
if age >= 18:#*因為age > 18 ,所以成立
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:#*不成立的就觸發
    print('your age is', age)
    print('teenager')
    
age = 3
if age >= 18:#%先判斷這種情況
    print('adult')
elif age >= 6:#%再判斷這個情況
    print('teenager')
else:#%全都不是的情況
    print('kid')
    
x= 2
if x:#*只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
    print('True')
    #