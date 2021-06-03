'''
Author: Swarfte_Tou
Date: 2021-05-12 22:25:48
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-12 22:35:22
FilePath: \Python\python_learn\進階的\StringIO和BytesIO.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%很多时候，数据读写不一定是文件，也可以在内存中读写

#%寫入StringIO的方法
import io
f = io.StringIO() #*StringIO用作在內存中讀寫str
a = f.write("hello world")#*a獲得的是字串的長度,並非真正的內容
print(a)
b = f.getvalue()#*通過getvalue函數獲得剛輸入的字串
print(b)

#%讀取StringIO的方法
c = io.StringIO('Hello!\nHi!\nGoodbye!')
s = c.read()
print(s)
