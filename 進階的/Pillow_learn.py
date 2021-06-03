import PIL.Image as PI
#% PIL 庫用作處理圖像 (需先安裝pillow)

test = PI.open("./PYTEST.jpg")#*這處用了相對路徑傳入圖片
x,y = test.size #*獲得照片的長和寬
print(f"長:{x} , 寬:{y} ")
test.thumbnail((x / 2 , y / 2))#*thumbnail用作縮放圖片,數值變化需用元祖表示,這裡是縮放為原來的一半
w,h = test.size
print(f"縮放後的長:{w} , 寬:{h} ")
test.save("cut_test.jpg","jpeg")

import PIL.ImageFilter as PIFT
photo = PI.open("./PYTEST.jpg")
fix_photo = photo.filter(PIFT.BLUR)#*為原圖片加入模擬效果,filter用作加特效
fix_photo.save("fix_photo.jpg","jpeg")

#%PIL庫也能直接生成圖片
import PIL.ImageDraw as PID
import PIL.ImageFont as PIF
import random as rd

def rdAZ () :#*生成隨機英文字母
    return chr(rd.randint(65, 90))#*返回ASCII碼65-90中的其中一個編碼,(65-90的編碼為大寫字母)

def rdColor1() : #*生成隨機顏色
    return (rd.randint(64,255),rd.randint(64,255),rd.randint(64,255))

def rdColor2(): #*生成隨機顏色(得一半區間)
    return (rd.randint(32,127),rd.randint(32,127),rd.randint(32,127))

x,y = 1920,1080
image = PI.new("RGB",(x,y),(255,255,255))#*創建一個圖片物件
font_use = PIF.truetype("arial.ttf",360)#*創建文字物件
font_number = 4
draw = PID.Draw(image)#*在image物件上覆蓋一層圖層
for a in range(x) :
    for b in range(y):
        draw.point((a,b),fill=rdColor1())#*fill為填充顏色,這裡填入隨機顏色,point用作填充像素點

for x in range(font_number) :
    draw.text((400 * x + 200,100 ),rdAZ(),font=font_use,fill=rdColor2())#*test用作生成文字,第一個參數為生成文字的位置,第2個參數為生成的字母,font參數指定字體,fill參數用作填充顏色

image.save("code.jpg","jpeg")#*保存處理好的圖片
