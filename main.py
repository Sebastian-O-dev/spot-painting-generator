import colorgram # This requires to instal colorgram.py package from pypi
import turtle
import random

rgb_colors = []

colors = colorgram.extract("image.jpg", 30)

for color in colors:
        rgb_colors.append(color.rgb[:])

print(rgb_colors)

color_bank = rgb_colors[4:]

tim = turtle.Turtle()
tim.speed("fastest")
tim.hideturtle()
screen = turtle.Screen()
screen.screensize(1080,720)
screen.colormode(255)

tim.penup()
tim.goto(-250,-250)
tim.pendown()

for ver_move in range(10):
    tim.penup()
    tim.goto(-250, (-250 + ver_move * 50))
    tim.pendown()
    for hor_move in range(10):
        tim.dot(20, random.choice(color_bank))
        tim.pu()
        tim.forward(50)
        tim.pd()


screen.exitonclick()
