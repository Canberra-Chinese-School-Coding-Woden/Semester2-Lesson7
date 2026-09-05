import turtle
import random

# ---------- Setup ----------
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0)
t.pensize(1)
t.pencolor("black")
t.fillcolor("orange")
screen.bgcolor("darkblue")
screen.setup(1000, 500)

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def five_pointed_star():
    t.begin_fill()

    colour = random.choice(["orange","yellow","gold"])
    t.fillcolor(colour)

    side_length = random.randint(50,100)
    for i in range(5):
        t.forward(side_length)
        t.left(215)
    
    t.end_fill()

def cloud():
    t.fillcolor("lightsteelblue")
    t.setheading(0)
    t.begin_fill()
    for i in range(18):
        t.forward(8)
        t.left(20)
    t.forward(50)
    for i in range(18):
        t.forward(13)
        t.left(20)
    t.forward(50)
    for i in range(18):
        t.forward(8)
        t.left(20)
    t.left(90)
    t.forward(20)
    for i in range(18):
        t.forward(4)
        t.left(20)
    t.end_fill()

def draw_moon():
    t.setheading(0)
    t.fillcolor("azure")
    t.begin_fill()
    for i in range(18):
        t.forward(20)
        t.left(10)
    t.forward(85)
    t.right(180)
    for i in range(18):
        t.forward(20)
        t.right(10)
    t.end_fill()


for i in range(30):
    five_pointed_star()
    go(random.randint(-500,500),random.randint(-250,250))

for i in range(15):
    cloud()
    go(random.randint(-500,500),random.randint(-250,-150))

go(0,0)
draw_moon()




