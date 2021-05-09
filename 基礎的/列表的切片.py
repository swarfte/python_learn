'''
Author: Swarfte_Tou
Date: 2021-05-09 21:26:19
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-09 21:49:06
FilePath: \python\python_learn\列表的切片.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
L = list(range(10))
S = L[0:3]#*利用切片獲得前3個元素(由0開始,到3結束(即0,1,2))
print(S)
A = L[:3]#*也可以忽略不視,:號前無數字默認由0開始
print(A)
C = L[-2:]#*由倒數第2個元素開始取,直至到最後一個元素
print(C)
O = L[:]#*:號前後都無數字則由頭取到尾
Z = list(range(100))
A2 = Z[::5]#*由頭到尾,每5個元素取一個(每隔四個元素取一次)
print(A2)
LZ = Z[::-1]#*由頭到尾,整數順序反轉,然後每1個元素取1個
print(LZ)