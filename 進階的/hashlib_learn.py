import hashlib as hs
#%摘要算法把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
test = hs.md5()#*創建一個MD5物件
test.update("你在幹甚麼".encode('utf-8'))#*必須encode對應的編碼
print(test.hexdigest())#*计算出一个字符串的MD5值

#%如果数据量很大，可以分块多次调用update()
testing = hs.md5()
testing.update("你在幹甚麼".encode("utf-8"))
testing.update("起飛".encode("utf-8"))#*对任意长度的数据data计算出固定长度的摘要digest
#print(testing)#*返回一個物件
print(testing.hexdigest())


#&測試一 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False
def test () :
    db = {#*數據庫
        'michael': 'e10adc3949ba59abbe56e057f20f883e',
        'bob': '878ef96e86145580c38c87f0410ad153',
        'alice': '99b1c2188db85afee403b1536010c2c9'
    }

    def login(user, password):#*驗證程式
        check = hs.md5()
        check.update(password.encode('utf-8'))
        use = check.hexdigest()
        for x in db :
            if x == user and db[x] == use :
                return True
        return False

    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')

if __name__ == "__main__" :
    test()