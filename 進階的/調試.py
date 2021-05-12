'''
Author: Swarfte_Tou
Date: 2021-05-12 21:59:11
LastEditors: Swarfte_Tou
LastEditTime: 2021-05-12 22:09:01
FilePath: \Python\python_learn\進階的\調試.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
GithubURL: https://github.com/swarfte/Swarfte.git
GithubLazy: git init git commit -m git push -u
'''
#%如果断言失败，assert语句本身就会抛出AssertionError
def test(s) :
    n = int(s)
    assert n != 0, 'n is zero!' #*assert是斷言, 斷言用作判斷一些條件/情況,如果通過不了斷言,根据程序运行的逻辑,那麼接下來的情式很有可能出錯
    return 10 / n

# test("0")#*0的時候通過不了斷言

import logging as log
just = int("0")
log.info(f"number = {just}")#*和assert比，logging不会抛出错误，而且可以输出到文件
#print(10/just)

import pdb
number = int("0")
pdb.set_trace()#* 运行到这里会自动暂停,程序会自动在pdb.set_trace()暂停并进入pdb调试环境,可以用命令p查看变量,或者用命令c继续运行
print(10 / number)