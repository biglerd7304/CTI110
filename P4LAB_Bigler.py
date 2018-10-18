# CTI-110
# P4LAB
# Daniel Bigler
# 9-18-18
#

def main():
    #get the turtle
    import turtle
    tur = turtle.Turtle()
    tur.shape("turtle")
    wn = turtle.Screen()
    #set up where it starts
    tur.penup()
    tur.backward(100)
    tur.pendown()
    #star
    #loop for the pentagon
    for i in range(1,6):
        #loop for the triangle
        for i in range(1,4):
            tur.forward(50)
            tur.right(120)
        tur.forward(50)
        tur.left(72)
    #set up position for snowflake
    tur.penup()
    tur.forward(200)
    tur.pendown()
    #snowflake
    #hexagon base
    for i in range(1,7):
        tur.right(60)
        #branches
        for i in range (1,4):
            tur.forward(10)
            tur.right(60)
            tur.forward(10)
            tur.backward(10)
            tur.left(120)
            tur.forward(10)
            tur.backward(10)
            tur.right(60)
        tur.backward(30)
        tur.left(120)
        tur.forward(10)
    #move turtle out of the way so you can see them clearly
    tur.penup()
    tur.forward(50)
    tur.left(90)
    tur.forward(200)
    tur.left(90)
    print("star and snowflake using nested loop")
main()
