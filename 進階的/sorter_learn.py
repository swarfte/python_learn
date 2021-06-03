'''
Author: Swarfte_Tou
Date: 2021-05-10 18:22:16
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-10 18:53:29
FilePath: \python\python_learn\進階的\sorter.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%sorted()函数用作排序
L = [11,8,99,45,32,4,66]
S = sorted(L)#*能單純用作排序
print(S)

#######################
LT = [11,8,99,45,32,4,66]
#%用另一種易懂的方式實現(泡沫排序法)
save = 0
for x in range(len(LT)) :#*一共要排序n次
    for j in range((len(LT)-x - 1)):#*由左至右開始排序,當第1個數字進行比較時,需要由左至右都比較一次(自身不用比較),所以為總長度-1,當第2個數開始時,則由第2位開始,比上一次減少比較1,如此累推,當去到最後一個數字時,就不用比較了
        if LT[j] > LT[j+1] :#*假如左邊的數大於右邊
            LT[j],LT[j+1] = LT[j+1],LT[j]#*兩個數字互相交換位置
print(LT)#*結果和sorted()一樣,而且sorted會比這種算法快

#%sorted()函数可以接收一个key函数来实现自定义的排序
J = [-8,-6,-99,-44,-2,89,12,5]
G = sorted(J,key=abs)#*key函數是abs(絕對值),結果會按照絕對值後排序
print(G)

#%想要反向結果的話,可以加入reverse參數
I = sorted(J,key=abs,reverse = True)
print(I)#*結果和G的完全反過來

#%sorted()函數也能用在大小寫排序
K =  sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)#*str.lower是字符串的小寫
print(K)#*按a-z,小寫到大寫的形式排序


