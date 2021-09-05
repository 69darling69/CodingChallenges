import math
import turtle


def branch(len):
    turtle.down()
    turtle.forward(len)
    turtle.up()
    if len <= 4:
        return

    stack.append(turtle.pos())
    turtle.right(angle)
    branch(len * scale)
    turtle.goto(stack.pop())
    stack.append(turtle.pos())
    turtle.left(2 * angle)
    branch(len * scale)
    turtle.goto(stack.pop())
    turtle.right(angle)


angle = math.degrees(math.pi / 6)
length = 200
scale = 2 / 3

WIDTH, HEIGHT = turtle.screensize()
turtle.speed(0)
turtle.up()
turtle.goto(0, -HEIGHT)
turtle.setheading(90)
stack = []

branch(length)

turtle.exitonclick()
