# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst_colours.jpg', 15)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

from turtle import Turtle, Screen
import random

t = Turtle()

screen = Screen()
screen.colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()

t.setheading(225)
t.forward(300)
t.setheading(0)

colors = [(46, 104, 159), (144, 179, 190), (225, 171, 125), (184, 148, 160), (125, 81, 90), (127, 73, 53), (37, 48, 65), (111, 174, 125), (214, 80, 58), (70, 6, 23), (40, 131, 105)]

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    t.dot(20, random.choice(colors))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen.exitonclick()