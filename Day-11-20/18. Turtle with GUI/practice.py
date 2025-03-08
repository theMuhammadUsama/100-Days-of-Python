#Ways of importing modules
#import turtle
#from turtle import Turtle
#from turtle import *
#import turtle as t

import turtle as t
import random

t.shape("turtle")
t.color("black")

# Making a square
# for i in range(4):
#     t.fd(100)
#     t.right(90)
# Making a dashed line
# for _ in range(15):
#     t.fd(10)
#     t.color('white')
#     t.fd(10)
#     t.color('black')

#Drawing Geometrical shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         t.fd(100)
#         t.right(angle)

# for shape_side_n in range(3, 11):
#     t.color(random_color())
#     t.width(5)
#     draw_shape(shape_side_n)
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Random Walk
# directions = [0, 90, 180, 270]
# t.speed("fastest")
# t.pensize(10)
# for i in range(200):
#     t.color(random_color())
#     t.forward(20)
#     t.setheading(random.choice(directions))

# Drawing a Spirograph
move = 5
t.speed("fastest")
for i in range (int(360/move)):
    t.color(random_color()) 
    t.circle(100)
    t.left(move)


screen = t.Screen()
screen.exitonclick()