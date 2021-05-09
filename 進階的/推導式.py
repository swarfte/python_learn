'''
Author: Swarfte_Tou
Date: 2021-05-09 21:53:45
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 22:02:01
FilePath: \python\python_learn\推導式.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''

print( [x * x for x in range(1, 11)])#*推導式寫法

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)#*一般的寫法

A = [x * x for x in range(1, 11) if x % 2 == 0]#*for循环后面还可以加上if判断,即x被2整除才會成立
print(A)
B = [m + n for m in 'ABC' for n in 'XYZ']#*可以使用两层循环，可以生成全排列
print(B)

PP = {'x': 'A', 'y': 'B', 'z': 'C' }
C = [k + '=' + v for k, v in PP.items()]#*推導式也支援多個變量,item()這個函數用作以列表的形式反回(键, 值) 的元组数组

D = [x if x % 2 == 0 else -x for x in range(1, 11)]#*若要使用if-else寫法則需要放在for前
print(D)

#%總結:推導式中,for 前的 if 為 表达式,for 後的 if 為篩選條件