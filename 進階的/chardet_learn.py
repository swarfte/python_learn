import chardet as cd 
print(cd.detect(b"hello world"))#*需要使用bytes來表示
#%检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。
test = "你在幹甚麼".encode('gbk')#*注意到GBK是GB2312的超集
print(cd.detect(test))#*檢測出編碼為windows-1251,命中率為34%,language為Bulgairan
use = "對不起我要起飛了".encode("utf-8")
print(cd.detect(use))#*檢測出編碼為utf-8,命中率為99%

#%可见，用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理。

