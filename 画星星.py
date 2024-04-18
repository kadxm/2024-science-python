import turtle
import random
t=turtle.Pen()
left=-(turtle.window_width()//3)
right=turtle.window_width()//3
top=turtle.window_height()//3
bottom=-(turtle.window_height()//3)
t.hideturtle()
t.speed(10000000000000000)
turtle.colormode(255)
turtle.bgcolor('black')
while True:
    x=random.randint(left,right)
    y=random.randint(bottom,top)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.color((r,g,b),(r,g,b))
    t.begin_fill()
    t.left(random.randint(0,90))
    lr=random.randint(50,300)
    for i in range(5):
        t.forward(lr)
        t.right(144)
    t.end_fill()
    t.penup()
    t.goto(x,y)
    t.pendown()
turtle.mainloop()