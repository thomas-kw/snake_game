from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")



starting_positions=[(0, 0), (-20, 0), (-40, 0)]

segments = []

# screen.tracer(0)

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)



game_is_on = True

while game_is_on:
    screen.update()
    for seg in segments:
        seg.forward(20)
        time.sleep(1)


















screen.exitonclick()