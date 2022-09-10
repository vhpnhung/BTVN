import math
import turtle

#set up ctct
hscr = turtle.Screen()
hscr.setup(1000, 1000)
htt = turtle.Turtle()
htt.pensize(5)
htt.speed(5)

def nha(cdn, cdm, wd, tc):

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
    htt.fd(cdn)
    htt.rt(45)
    htt.fd(cdm)
    htt.rt(90)
    htt.fd(cdm)
    htt.rt(45)
    htt.fd(cdn)
    htt.lt(90)
    htt.end_fill() #khung nha

    htt.penup()
    htt.goto(-300, cdn - 400)
    htt.pendown()
    htt.fillcolor("red")
    htt.begin_fill()
    htt.lt(45)
    htt.fd(cdm)
    htt.rt(90)
    htt.fd(cdm)
    htt.rt(135)
    htt.fd(math.sqrt(2)*cdm)
    htt.end_fill() #mai nha

    htt.penup()
    htt.goto(-math.sqrt(2)*cdm/3 + math.sqrt(2)*cdm - 300, -cdn/3 + cdn - 400)
    htt.pendown()
    htt.fillcolor("orange")
    htt.begin_fill()
    htt.fd(wd)
    htt.lt(90)
    htt.fd(wd)
    htt.lt(90)
    htt.fd(wd)
    htt.lt(90)
    htt.fd(wd)
    htt.lt(90)
    htt.rt(90)
    htt.end_fill() #cua so

    #ve cay
    htt.penup()
    htt.goto(math.sqrt(2)*cdm*1.5, 0)
    htt.pendown()
    htt.fillcolor("green")
    htt.begin_fill()
    htt.circle(tc)
    htt.end_fill() #la cay

    htt.penup()
    htt.goto(math.sqrt(2)*cdm*1.5 - tc, -400)
    htt.pendown()
    htt.pencolor("brown")
    htt.pensize(30)
    htt.fd(400) #than cay

    turtle.done()
    
nha(400,220,150,100)