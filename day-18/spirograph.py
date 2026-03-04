from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")

screen = Screen()
screen.colormode(255)

t.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        t.circle(100)
        t.color(random_color())
        t.setheading(t.heading() + gap_size)
        t.circle(100)

draw_spirograph(5)

screen.exitonclick()