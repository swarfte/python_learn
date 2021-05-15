'''
Author: Swarfte_Tou
Date: 2021-05-14 18:55:43
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-15 13:54:28
FilePath: \Python\python_learn\禿頭的\正則表達式.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%re模組用作實現正則表則式
import re 

STR = "1.ben go to school by bus with his friends JOJO. \n 1個月有7日!會做這樣的事14次。 Some time will play computer games in bedroom"

#%search函數用作在資料內搜索與篩選條件匹配的資料,第一個參數傳入要篩選條件,第2個參數傳入資料
a = re.search(r"ben",STR)#*字符串前跟r表示為原始字符串
print(f"a :{a}")#*search函數會反回一個對像,對像包含"第一個"匹配成功的資料,和其所在的位置(起始,結束)
b = re.search(r"plays",STR)#*沒有找到則返回None
print(f"b :{b}")
c = STR.find("go")
print(f"c :{c}")#*find()會返回匹配字串的起始位置(下標)
d = re.search(r"JO.",STR)#*在正則表達式中,"."用作通配符,即用於匹配任何字符(除換行符\n)
print(f"d :{d}")
e = re.search(r"JO..\.",STR)#*用"\"表示轉義字符
print(f"e :{e}")
f = re.search(r"\d",STR)#*在正則表達式中,\d表示匹配數字,等價於[0-9]
print(f"f :{f}")
g = re.search(r"[aeiou]",STR)#*[]內的為字符類,同時在字符類的元字符都失去了特殊功廳,只要資料中出現與[]內相同的字符,則匹配成立
print(f"g :{g}")
h = re.search(r"[a-z]",STR)#*可以用"-"號表示匹配範圍
print(f"h :{h}")
i = re.search(r"[0-9]\.[a-z][a-z][a-z]",STR)#*"-"號表示範圍 數字也能表示範圍
print(f"i :{i}")
j = re.search(r"[sch]{3}.{3}",STR)#*在正則表達式中,用{}表示該篩選條件的重覆次數
print(f"j :{j}")
k = re.search(r"[schol]{1,5}",STR)#*{}可輸入最小和最大的匹配次數,{1,5}和{2,5}的結果有很大差別
print(f"k :{k}")
l = re.search(r"[be]{3} | [sch]{3}",STR)#* "|"號在正則表達底中充當"或"的作用
print(f"l :{l}")
m = re.search(r"[JO]{2,}",STR)#*{2,s}表示最少匹配2次才算成立,匹配成功時會一直配對(預設貪婪模式)
print(f"m :{m}")
n = re.search(r"[friends]{,5}",STR)#*{,5}表示最多匹配5次,結果為" ",因為可以一次也不匹配
print(f"n :{n}")
#% * , + , ? 預設開啟貪婪模式,即盡可能匹配多的字元
o = re.search(r"[bus]*",STR)#* "*"號表示{0,}
print(f"o :{o}")
p = re.search(r"[with]+",STR)#* "+"號表示{1,0}
print(f"p :{p}")
q = re.search(r"[his]?",STR)#* "?"號表示{0,1} 可理解為可有可無
print(f"q :{q}")
#% 在 * , + ,? 後跟 "?"號即開啟非貪婪模式,即只匹配剛好滿足條件的情況(匹配最少的字串符)
r = re.search(r"[bus]*?",STR)#* 因為*號本身匹配{0,},非貪婪即0次
print(f"r :{r}")
s = re.search(r"[with]+?",STR)#* 因為+號為{1,0},則只匹配一個滿足該條件的字符
print(f"s :{s}")
t = re.search(r"[his]??",STR)#* {0,1}則0次
print(f"t :{t}")

RAN = "wrdascxz192.168.0.1cxzjaksdjw岸昊蚱未因"

u = re.search(r"(\d\d\d\.){2}",RAN)#*小括號用於表示一個整體
print(f"u :{u}")
v = re.search("(([0-1]?\d?\d|2[0-4]\d|25[0-5])\.){3}([0-1]?\d?\d|2[0-4]\d|25[0-5])",RAN)#*用正式表達式表示IP的方法
print(f"v :{v}")#*其實前後兩部份一樣,但最後那個數後面不跟小數點,所以分成兩部份
w = re.search(r"^\d\.[ben]+",STR)#* "^"號表示匹配字符串的開始位置,即當第一個字符滿足條件才會匹配
print(f"w :{w}")
x = re.search(r"[rom]+$",STR)#* "%"號素示匹配字符串的結束位置,即最後一個字符滿足條件時才會匹配
print(f"x :{x}")
y = re.search(r"[^a-z]+",STR)#* 在[]號,"^"號能表示取反的意思,即匹配除a-z的字符
print(f"y :{y}")
z = re.search(r"\bby\b",STR)#* \b表示匹配一個單詞的邊界, 即表示 "by" 這個字串前後不能是字母/空格/下劃線才會匹配成功
print(f"z: {z}")
AA = re.search(r"\bshool\b",STR)#*這時匹配不成功,因為school後跟了s ,這表示school並不是一個獨立的單詞
print(f"AA :{AA}")
BB = re.search(r"\Briend\B",STR)#* \B的作用興\b相反,用作匹配非單詞邊界,即 "riend" 的前後要跟英文字母/數字才會匹配成功
print(f"BB :{BB}")
CC =re.search(r"\D+",STR)#* \D的作用剛好和\d相反,匹配非數字的字符,等價於[^0-9]
print(f"CC :{CC}")
DD = re.search(r"\D\s\d",STR)#* \s表示匹配任何空白字符
print(f"DD :{DD}")
EE = re.search(r"\d\S+",STR)#* \S則表示匹配任何非空白字符
print(f"EE :{EE}")
FF = re.search(r"\t",STR)#* \t表示匹配tab鍵(默認4個空格)
print(f"FF :{FF}")
GG = re.search(r"\n\s\S+",STR) #* \n 表示匹配換行,即字符串中的\n
print(f"GG :{GG}")
HH = re.search(r"\d\w+",STR)#* \w表示匹配單詞,即中英數都能匹配,但會被空格等符號限制
print(f"HH :{HH}")#*和\S+不同,/w遇到標點符號便會停止
II = re.search(r"\W+",STR)#* \W和\w 相反,用作匹配標點符號和空格等字符
print(f"II :{II}")