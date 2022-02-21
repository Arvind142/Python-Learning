import turtle

# actual code
cir=turtle.Turtle()
cir.color('red')
sq=turtle.Turtle()
sq.color('green')
# box - circle
for i in range(36):
    # circle
    cir.forward(4.4)
    cir.left(10)
    # square
    sq.forward(50)
    sq.left(90)
turtle.done()