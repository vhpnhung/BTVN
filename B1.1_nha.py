import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.pensize(5)

def des_house(size, floor):
    for tang in range(floor):
        for i in range(4):
            t.fd(size)
            t.rt(90)
        t.penup()
        t.lt(90)
        t.fd(size)
        t.pendown()
        t.rt(90)
    turtle.done()

des_house(50,4)