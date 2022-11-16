import turtle
import sys


def generate1(n, result='X'):
    for _ in range(n):
                
        # RULE 1
        result = result.replace('F', 'FF')

        # RULE 2
        result = result.replace('X', '--FXF++FXF++FXF--')

    return result



def draw(cmds, size, angle):
    stack = []
    for cmd in cmds:
        if cmd=='F':
            turtle.pendown()
            turtle.forward(size)
        elif cmd=='X':
            pass
        elif cmd=='Y':
            turtle.pendown()
            turtle.forward(size)
        elif cmd=='-':
            turtle.left(angle)
        elif cmd=='+':
            turtle.right(angle)
        else:
            raise ValueError('Unknown Cmd: {}'.format(ord(cmd)))
    turtle.update()


def setup():
    turtle.hideturtle()
    turtle.tracer(1e3,0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


setup()
triangle = generate1(6)
draw(triangle, 5, 60)
setup()
draw(triangle, 5, -60)
