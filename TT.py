import turtle

okscr = turtle.Screen()
okscr.setup(1000, 1000)

oktt = turtle.Turtle()
oktt.pensize(5)
oktt.pencolor("pink")
oktt.fillcolor("black")
oktt.begin_fill() #phai begin thi moi co fill

#ve hinh tron
oktt.circle(50)

oktt.end_fill() #Luc nay moi co mau fill ne

#ve hinh chu nhat, dung lenh co bien
a=50
b=100 #gan gia tri cho bien

oktt.penup()
oktt.fd(200)
oktt.pendown() #di chuyen vi tri

oktt.begin_fill()
oktt.fd(a)
oktt.lt(90)
oktt.fd(b)
oktt.lt(90)
oktt.fd(a)
oktt.lt(90)
oktt.fd(b)
oktt.lt(90)
oktt.end_fill() #ve hinh chu nhat

turtle.done()