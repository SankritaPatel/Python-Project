#Write a program to display the multiplication table from 1 to 10 in the Turtle graphics window 
import turtle as t
t.penup()
x = -100
y =  100
t.goto(x,y)
t.penup()
for i in range(1,11,1):
    y = y-20
    for j in range(1,11,1):
        t.penup()
        t.speed(1)
        t.forward(20)
        t.write(i*j)
    t.goto(x, y)