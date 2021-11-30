import turtle as t
import math as m
import random


t.bgcolor("black")
t.speed(0)

q = 100000
n = 0


def rose():
    t.color("red")
    t.pendown()
    p=t.xcor()
    for n in range(150):
        global q
        t.pensize(int(m.exp(n/100)))
        t.forward(n/2)
        t.left(70)
        if (q > t.ycor()):
            q = t.ycor()
    t.penup()

    t.goto(p, q)
    t.setheading(t.towards(0, -300))

    t.color("darkgreen")
    t.pensize(10)

    d = t.distance(0, -300)

    t.pendown()
    for j in range(15):
        t.forward(d/30)
        t.left(90)
        t.stamp()
        t.right(90)
        t.forward(d/30)
        t.right(90)
        t.stamp()
        t.left(90)
    t.penup()


t.penup()


t.goto(0, -300)

l = int(input("장미 밭에는 몇 송이의 장미가 있나요? : "))

for k in range(l):
    x_start = random.randrange(-500, 501)
    y_start = random.randrange(0, 300)

    t.goto(x_start, y_start)

    rose()

    q = 10000


t.done()











