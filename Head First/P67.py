phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)

### 最大行數:8行
plist.pop(0)
plist.pop(2)
plist.insert(2, " ")
for x in range(6):
    plist.pop()
plist.append("a")
plist.append("p")
###

new_phrase = "".join(plist)
print(plist)
print(new_phrase)
