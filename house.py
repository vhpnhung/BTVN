import turtle

#set up ctct
hscr = turtle.Screen()
hscr.setup(1000, 1000)
htt = turtle.Turtle()
htt.pensize(5)
htt.speed(0)

#ve mat dat
htt.penup()
htt.goto(-400, -400)
htt.pendown()
htt.fd(800)

#ve nha
htt.fillcolor("pink")
htt.begin_fill()
htt.penup()
htt.goto(-300, -400)
htt.pendown()
htt.lt(90)
htt.fd(300)
htt.rt(45)
htt.fd(200)
htt.rt(90)
htt.fd(200)
htt.rt(45)
htt.fd(300)
htt.lt(90)
htt.end_fill() #khung nha

htt.penup()
htt.goto(-300, -100)
htt.pendown()
htt.fillcolor("red")
htt.begin_fill()
htt.lt(45)
htt.fd(200)
htt.rt(90)
htt.fd(200)
htt.rt(135)
htt.fd(280)
htt.end_fill() #mai nha

htt.penup()
htt.goto(-100, -200)
htt.pendown()
htt.fillcolor("orange")
htt.begin_fill()
htt.fd(100)
htt.lt(90)
htt.fd(100)
htt.lt(90)
htt.fd(100)
htt.lt(90)
htt.fd(100)
htt.lt(90)
htt.rt(90)
htt.end_fill() #cua so

#ve cay
htt.penup()
htt.goto(400, 0)
htt.pendown()
htt.fillcolor("green")
htt.begin_fill()
htt.circle(200)
htt.end_fill() #la cay

htt.penup()
htt.goto(200, -400)
htt.pendown()
htt.pencolor("brown")
htt.pensize(30)
htt.fd(400) #than cay

turtle.done()