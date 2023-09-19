import turtle
turtle.hideturtle()
def square(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
for i in range(1, 10):
    square(i*10)
