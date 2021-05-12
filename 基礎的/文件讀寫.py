'''
Author: Swarfte_Tou
Date: 2021-05-12 22:14:50
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-12 22:25:23
FilePath: \Python\python_learn\基礎的\文件讀寫.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%读取文件
with open("./test.txt","r",encoding="utf-8") as test :#* "r"是唯讀模式, as test 是指用test來代替該文件,encoding用作指定編碼內容
    print(test.read())#*讀取文件的內容,#*read函數可傳入size參數,控制每次讀取的數量
    
#%編輯文件
with open("./test.txt","w") as b :#* "a"模式用作續寫,"w"模式覆蓋/重寫
    b.write("文件讀寫.py的範本")#*在原有的文本後續寫

#%所有模式的定义及含义可以参考Python的官方文档。