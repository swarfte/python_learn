import turtle as tt
import random as rd
#%turtle模組用作畫圖
def simple_rectangle():#&用基本的方法畫一個長方形
    tt.width(3)#*設置海龜的筆刷長度
    tt.pencolor("green")#*設置畫筆的顏色
    tt.forward(200)#*前進 200 碼
    tt.right(90)#*右轉 90 度
    
    tt.width(4)#*設置海龜的筆刷長度
    tt.pencolor("red")#*設置畫筆的顏色
    tt.forward(100)#*前進 200 碼
    tt.right(90)#*右轉 90 度
    
    tt.width(5)#*設置海龜的筆刷長度
    tt.pencolor("blue")#*設置畫筆的顏色
    tt.forward(200)#*前進 200 碼
    tt.right(90)#*右轉 90 度
    
    tt.width(6)#*設置海龜的筆刷長度
    tt.pencolor("black")#*設置畫筆的顏色
    tt.forward(100)#*前進 200 碼
    tt.right(90)#*右轉 90 度

    tt.done()#*done 指定用作等待結束 ,否則畫完圖後會馬上退出

def square():#*畫一個隨機的正方形
    foot = rd.randint(100,300)
    color = ["red","blue","black","green","yellow","pink"]
    for x in range(4) :
        tt.width(rd.randint(1,10))
        tt.pencolor(color[rd.randint(0,5)])
        tt.forward(foot)
        tt.right(90)
    tt.done()

def five_star():#*畫一個五角星, x和y為起始的座標
    def star_write(x,y):#*五角星每條邊的移動
        tt.pu()#*拿起畫筆,此時移動不會留下路線
        tt.goto(x,y)#*移動至指定座標
        tt.pd()#*放下畫筆
        tt.seth(0)#*設置"海龜"面向的角度
        for x in range(5):#*5角星當然移動5次
            tt.fd(40)#*fd為forward的縮寫
            tt.rt(144)#*rt為right的縮寫
    for x in range(0,250,50):#*這裡是畫5顆五角星,因為250/50 = 5
        star_write(x,0)
    tt.done()

r = 0
g = 0
b = 0
def big_tree():#*也能畫一顆分型樹
    global r,g,b
    tt.colormode(255) #*设置色彩模式是RGB:

    tt.lt(90)#*left左轉的縮寫

    lv = 14
    l = 120
    s = 45

    tt.width(lv)
    tt.pencolor(r, g, b)#*設置RGB顏色

    tt.penup()#*拿起筆
    tt.bk(l)#*back後退的縮繫
    tt.pendown()#*放下筆
    tt.fd(l)

    def draw_tree(l, level):
        # save the current pen width
        global r,g,b
        w = tt.width()#*獲得畫筆粗度

        # narrow the pen width
        tt.width(w * 3.0 / 4.0)#*更改畫筆粗度
        # set color:
        r = r + 1
        g = g + 2
        b = b + 3
        tt.pencolor(r % 200, g % 200, b % 200) #*更改畫筆顏色

        l = 3.0 / 4.0 * l

        tt.lt(s)
        tt.fd(l)

        if level < lv:
            draw_tree(l, level + 1)
        tt.bk(l)
        tt.rt(2 * s)
        tt.fd(l)

        if level < lv:
            draw_tree(l, level + 1)
        tt.bk(l)
        tt.lt(s)

        # restore the previous pen width
        tt.width(w)

    tt.speed("fastest")#*設置畫筆速度

    draw_tree(l, 4)

    tt.done()

if __name__ == '__main__':
    #simple_rectangle()
    #square()
    #five_star()
    big_tree()
    pass