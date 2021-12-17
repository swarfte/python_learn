# #裝飾器工廠的定義
# # def 裝飾器工廠的名稱(參數名稱, ....)
# #   def 裝飾器名稱(回呼函式名稱):
# #       def 內部函式名稱():
# #           #裝飾器內部的程式碼
# #           回呼函式名稱()
# #       return 內部函式名稱
# #   return 裝飾器名稱

# # 基本裝飾器工廠的用法
# def myFactory(base):#傳入額外的     參數用作生產裝飾器(裝飾器工廠的作用)
#     def myDeco(cb):#基本的裝飾器
#         def run():
#             print("裝飾器內的程式碼",base)
#             result=base**2
#             cb(result)
#         return run
#     return myDeco

# @myFactory(3)
# def test(result):
#     print("普通函式的程式",result)

# test()


# 計算1+2+3+....+n的裝飾器工廠
def calculateFactory(max):#在基本裝飾器上加上工廠
    def calculate(cb):
        def run():
            total = 0
            for x in range(max+1):
                total +=x
            cb(total)
        return run
    return calculate

@calculateFactory(100)
def show(result):
    print("結果是",result)

@calculateFactory(100)
def showEnglish(result):
    print("result is",result)
    
show()
showEnglish()