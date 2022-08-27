import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.pensize(5)
t.speed(0)

r = int(input("Nhap ban kinh: "))
slg = int(input("So luong canh hoa: "))
goc_quay = 0

while goc_quay < 360:
    t.circle(r)
    t.rt(360/slg)
    goc_quay += (360/slg)
    
turtle.done()