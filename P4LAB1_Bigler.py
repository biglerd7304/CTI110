# CTI-110
# P4LAB1
# Daniel Bigler
# 9-2-18
#

def main():
    import turtle
    t = turtle.Turtle()
    t.shape("turtle")
    wn = turtle.Screen()
    for i in [0,1,2,3]:
        t.forward(50)
        t.left(90)
    for i in [0,1,2]:
        t.forward(50)
        t.right(120)
main()
