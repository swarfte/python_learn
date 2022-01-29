from setuptools import setup

# *更新模組時也是重覆這三個步驟,但要一個新的版本號
# 創建一個發佈描述 在windows下執行 py -3 setup.py sdist 後生成一個dist檔
setup(  # name 和 py_modules 是必須的,共他是可選的
    name="vsearch",
    version="1.0",
    description="SequentialStack and postfix expression calc",
    author="Swarfte",
    url="wcpbenchau@gmail.com",
    py_modules=["vsearch"]
)

# 出現dist檔以及removing 'name-version' (and everything under it) 說明第一步完成了
# 接下來進入cd dist 進入dist檔內 並執行 py -3 -m pip install name-version.tar.gz
# 執行後出現 Successfully installed name-version 後即為OK


# 更新簡要說明:
# 第一步 py -3 setup.py sdist
# 第二步 cd dist
# 第三步 py -3 -m pip install name-version.tar.gz
