import turtle

turtle.speed(0)
turtle.bgcolor('black')

for i in range(100):
    for colour in ["red", "white", "magenta", "green", "cyan", "yellow", "blue"]:
        turtle.color(colour)
        turtle.pensize(3)
        turtle.left(10)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200) 
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)