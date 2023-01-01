from turtle import *

title("五星红旗")
colormode(255)
setup(1250,850,10,10)
screensize(1250,850,"red")
pensize(2)
pencolor(255,222,0)
fillcolor(255,222,0)
speed(0)

#大五角星
penup()
goto(-560,220)
pendown()
begin_fill()
for i in range(5):
    fd(70)
    left(72)
    fd(70)
    right(144)
end_fill()

#第一个小五角星
penup()
goto(-350,350)
seth(-20)
pendown()
begin_fill()
for i in range(5):
    fd(30)
    left(72)
    fd(30)
    right(144)
end_fill()

#第二个
penup()
goto(-350,80)
seth(-20)
pendown()
begin_fill()
for i in range(5):
    fd(30)
    left(72)
    fd(30)
    right(144)
end_fill()

#第三个
penup()
goto(-230,280)
seth(-40)
pendown()
begin_fill()
for i in range(5):
    fd(30)
    left(72)
    fd(30)
    right(144)
end_fill()

#第四个
penup()
goto(-240,130)
seth(0)
pendown()
begin_fill()
for i in range(5):
    fd(30)
    left(72)
    fd(30)
    right(144)
end_fill()
hideturtle()

done()






