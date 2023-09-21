import turtle as t
#Created By Yogendra prasad SYIT 2023-2024
s = t.Screen()
s.bgcolor('gray')

t.speed(0)
t.pensize(8)
t.penup()
t.left(90)
t.forward(250)
t.left(90)
t.forward(400)
t.left(180)
t.pendown()

t.pencolor("orange")
t.pensize(4)
t.forward(124) #line
t.backward(117)
t.pencolor("dark blue")
t.pensize(8)
t.penup()
t.left(90)
t.forward(10)
t.pendown()
t.forward(50) #t
t.backward(7)
t.left(90)
t.forward(7)
t.backward(14)
t.penup()
t.backward(10)
t.pendown()
t.backward(100)
t.penup()
t.forward(90)
t.left(70)
t.forward(20)
t.pendown()
for i in range(30):
	t.backward(1)
	t.right(5)

def ll():
    for i in range(30):
        t.forward(1)
        t.left(5)
ll() #c
t.left(19)
t.forward(15)
ll()
t.left(-60)
t.penup()
t.forward(15)
t.pendown()
t.left(300) #s
for i in range(3):
    t.backward(1.18)
    t.right(8)
for i in range(30):
    t.forward(1.18)
    t.left(8)
t.forward(7.95)
for i in range(30):
    t.forward(1.18)
    t.right(8)
t.penup()
t.forward(6)
t.left(90)
t.forward(35)
t.pendown()
t.left(100)
ll() #c
t.left(19)
t.forward(15)
ll()