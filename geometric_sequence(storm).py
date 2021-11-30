import turtle as t

t.color('black')
t.speed(0)
t.setheading(90)

radius = [200,]

for i in range(1, 150):
    radius.append(radius[i-1]*0.9)

for i in range(100):
    t.circle(radius[i], 180)

t.done()











