# CTI-110
# P4LAB2
# Daniel Bigler
# 9-2-18
#

def main():
    import turtle
    turk = turtle.Turtle()
    turk.shape("turtle")
    wn = turtle.Screen()
    wn.bgcolor("darkgreen")
    turk.color("lightgreen")
    turk.pensize(2)
    turk.penup()
    turk.backward(100)
    turk.left(90)
    turk.pendown()
    turk.forward(100)
    turk.right(90)
    turk.forward(10)
    for i in [0,1,2,3,4,5,6,7,8]:
        turk.forward(9)
        turk.right(20)
        turk.forward(9)
    turk.forward(10)
    turk.right(180)
    turk.penup()
    turk.forward(100)
    turk.pendown()
    turk.left(90)
    turk.forward(100)
    turk.right(90)
    turk.forward(10)
    for i in [0,1,2,3,4,5,6,7,8]:
        turk.forward(4)
        turk.right(20)
        turk.forward(4)
    turk.right(180)
    for i in [0,1,2,3,4,5,6,7,8]:
        turk.forward(5)
        turk.right(20)
        turk.forward(5)
    turk.forward(10)
main()
