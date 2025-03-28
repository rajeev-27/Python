from turtle import Turtle

ALIGN="center"
FONT=("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.point=0
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.write(f"Score: {self.point}", align=ALIGN, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.point}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)


    def increase_point(self):
        self.point += 1
        self.clear()
        self.update_score()


