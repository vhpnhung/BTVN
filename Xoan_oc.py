import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.pensize(5)

kc = int(input("Nhap khoang cach: "))
limit = int(input("Nhap gioi han: "))

while limit <= 0:
    limit = int(input("Nhap khoang cach: "))

while turtle.distance(t) < limit:
    t.fd(kc)
    t.lt(10)
    kc +=1

turtle.done()