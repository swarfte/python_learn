'''
Author: Swarfte_Tou
Date: 2021-05-14 18:55:43
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-15 00:01:57
FilePath: \Python\python_learn\禿頭的\正則表達式.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%re模組用作實現正則表則式
import re 

s = "1.ben go to school by bus with his friends JOJO. 1個月有7日會做這樣的事14次"

#%search函數用作在資料內搜索與篩選條件匹配的資料,第一個參數傳入要篩選條件,第2個參數傳入資料
a = re.search(r"ben",s)
print(a)#*search函數會反回一個對像,對像包含"第一個"匹配成功的資料,和其所在的位置(起始,結束)
b = re.search(r"play",s)#*沒有找到則返回None
print(b)
c = s.find("go")
print(c)#*find()會返回匹配字串的起始位置(下標)
d = re.search(r"JO.",s)#*在正則表達式中,"."用作通配符,即用於匹配任何字符(除換行符\n)
print(d)
e = re.search(r"JO..\.",s)#*用"\"表示轉義字符
print(e)
f = re.search(r"\d",s)#*在正則表達式中,\d表示匹配數字
print(f)
g = re.search(r"[aeiou]",s)#*[]內的為字符內,只要資料中出現與[]內相同的字符,則匹配成立
print(g)
h = re.search(r"[a-z]",s)#*可以用"-"號表示匹配範圍
print(h)
i = re.search(r"[0-9]\.[a-z][a-z][a-z]",s)#*數字也能表示範圍
print(i)
j = re.search(r"[sch]{3}.{3}",s)#*在正則表達式中,用{}表示該篩選條件的重覆次數
print(j)
k = re.search(r"[schol]{1,5}",s)#*{}可輸入最小和最大的匹配次數,{1,5}和{2,5}的結果有很大差別
print(k)
l = re.search(r"[be]{3} | [sch]{3}",s)#* "|"號在正則表達底中充當"或"的作用
print(l)
m = re.search(r"[JO]{2,}",s)#*{2,s}表示最少匹配2次才算成立,匹配成功時會一直配對(預設貪婪模式)
print(m)
n = re.search(r"[friends]{,5}",s)#*{,5}表示最多匹配5次,結果為" ",因為可以一次也不匹配
print(n)
o = re.search(r"[bus]*",s)#* "*"號表示{0,}
print(o)
p = re.search(r"[with]+",s)#* "+"號表示{1,0}
print(p)
q = re.search(r"[his]?",s)#* "?"號表示{0,1} 可理解為可有可無
print(q)
