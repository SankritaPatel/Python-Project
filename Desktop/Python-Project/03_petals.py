import turtle as t
t.hideturtle()
def petal(t,r,angle):
    for i in range(2):
        t.circle(r,angle)
        t.left(180-angle)
def flower(t,n,r,angle):
    for i in range(n):
        petal(t,r,angle)
        t.left(360.0/n)
flower(t,7,80.0,60.0)