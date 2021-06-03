'''
Author: Swarfte_Tou
Date: 2021-05-10 17:56:17
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-10 18:23:51
FilePath: \python\python_learn\進階的\map.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
def f(x):
    return x ** 2
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r = map(f, L)#*map函數的作用是把列表中的每個元素依次傳入該函數
print(r)#*map返回的是一個生成器
print(list(r))#*用list函數把結果輸出來

##################################
#%用一般的方法實驗
S = []
for x in L :
    S.append(f(x))
print(S)#*結果和用map一樣
