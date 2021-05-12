'''
Author: Swarfte_Tou
Date: 2021-05-12 22:42:12
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-12 22:58:04
FilePath: \Python\python_learn\進階的\os.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
import os
print(os.name)#*操作系统类型,如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
#print(os.environ)#* 查看環境變量 
#print(os.environ.get("PATH")) #*获取某个环境变量的值
print(os.path.abspath('.'))#*查看当前目录的绝对路径:
#%通过os.path.join()函数两个路径合成一个;os.path.split()函数把一个路径拆分为两部分,后一部分总是最后级别的目录或文件名
print(os.path.join("D:/1A/Python/python_learn/進階的","os_file"))#*把目录的路径表示出来
os.mkdir('D:/1A/Python/python_learn/進階的/os_file')#*mkdir用於创建一个目录(當目錄存在時就不能創建)
os.rmdir('D:/1A/Python/python_learn/進階的/os_file')#&rmdir用於剛除一个目录(當目錄不存在時就不能剛除)
#os.rename("os.py","os.txt")#*对文件重命名
#os.remove('os.py')#*删掉文件
a =[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'] #*找出當時工作路徑下的py檔
print(a)
