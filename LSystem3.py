import turtle
import sys
import math
import random


def randang(angle):
    angle = angle + (random.random()*1)
    return angle


def randsize(size):
 #   size = float(size*random.random())
    return size


def generate1(n, result='X'):
    for _ in range(n):
        # rule #2
        result = result.replace('F', 'FF')
        # rule #1
        result = result.replace('X', 'FX+F[F-X]')

    return result



def draw(cmds, size, angle):
    stack = []
    for cmd in cmds:
        if cmd=='F':
            turtle.forward(randsize(size))
        elif cmd=='-':
            turtle.left(randang(angle))
        elif cmd=='+':
            turtle.right(randang(angle))
        elif cmd=='X':
            pass
        elif cmd=='[':
            stack.append((turtle.position(), turtle.heading()))
        elif cmd==']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.setposition(position)
            turtle.setheading(heading)
            turtle.pendown()
        else:
            raise ValueError('Unknown Cmd: {}'.format(ord(cmd)))
    turtle.update()

def setup():
    turtle.hideturtle()
    turtle.tracer(1e3,0)
    turtle.left(90)
    turtle.penup()
 #   turtle.goto(0,-turtle.window_height()/2)
    turtle.goto(0, 0)
    turtle.pendown()

setup()
plant = generate1(7)
draw(plant, 2, 22)
