import turtle
import math

precision=5000  #设置精度为5000
data=[]

f=open("drawData.txt","r")  #生成数据
for line in f:
    line = eval(line)
    data.append(line)

n=len(data)+1
x=[0]*n
y=[0]*n

turtle.setup(960,720)   #建立画布
turtle.penup()
turtle.pensize(2)

for t in range(precision):    #复数运算
    for i in range(len(data)):
        if i % 2 == 0:
            x[i] = data[i][0] * math.cos(i / precision * 3.14 * t) - data[i][1] * math.sin(i / precision * 3.14 * t)
            y[i] = data[i][0] * math.sin(i / precision * 3.14 * t) + data[i][1] * math.cos(i / precision * 3.14 * t)

        else:
            x[i] = data[i][0] * math.cos(-(i+1) / precision * 3.14 * t) - data[i][1] * math.sin(-(i+1) / precision * 3.14 * t)
            y[i] = data[i][0] * math.sin(-(i+1) / precision * 3.14 * t) + data[i][1] * math.cos(-(i+1) / precision * 3.14 * t)

    turtle.goto(int(sum(x)), -int(sum(y))) # 正负可以控制图形的左右镜像，上下镜像,乘除可以控制缩放
    turtle.pendown()
