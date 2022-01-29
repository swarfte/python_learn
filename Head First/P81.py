phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)
### 最大行數 : 4行
plist = plist[1:3] + plist[5:6] + plist[4:5] + plist[7:8] + plist[6:7] # 即是 "on" + " " + "t" + "a" +"p" 組合起來
new_phrase = "".join(plist)
###
print(plist)
print(new_phrase)
