from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto((0, 280))
        self.color('white')
        self.points = 0
        self.score()

    def score(self):
        self.write(f"Score: {self.points}", align="center", font=("Arial", 15, "normal"))
