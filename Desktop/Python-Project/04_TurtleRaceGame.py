import random, turtle
turtle.hideturtle()
myscreen = turtle.Screen()
myscreen.title("Turtle Race Game")
myscreen.bgcolor('pink')
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-200,200)
pen.pendown()
for i in range(1,11):
    pen.setheading(-90)
    pen.forward(250)
    pen.back(250)
    pen.penup()
    pen.setheading(0)
    pen.forward(50)
    pen.pendown()
finishLineX = 250
#create turtle players
def createplayer(color, startx, starty):
    player = turtle.Turtle()
    player.color(color)
    player.shape("turtle")
    player.penup()
    player.goto(startx, starty)
    player.pendown()
    return player
p1 = createplayer('red', -210, 150)
p2 = createplayer('blue', -210, 100)
p3 = createplayer('orange', -210, 50)
p4 = createplayer('green', -210, 0)
while True:
    p1.forward(random.randint(5,10))
    if p1.pos() [0]>= finishLineX:
        p1.write('I won the race!',font = ('Arial',30))
        break
    p2.forward(random.randint(5,10))
    if p2.pos() [0]>= finishLineX:
        p2.write('I won the race!',font = ('Arial',30))
        break
    p3.forward(random.randint(5,10))
    if p3.pos() [0]>= finishLineX:
        p3.write('I won the race!',font = ('Arial',30))
        break
    p4.forward(random.randint(5,10))
    if p4.pos() [0]>= finishLineX:
        p4.write('I won the race!',font = ('Arial',30))
        break
turtle.done()