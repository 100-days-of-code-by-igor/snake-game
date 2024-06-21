from turtle import Turtle
FONT = ('Courier', 15, 'bold')
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.setposition(0, 275)

    def show_score(self):
        self.write(arg=f"Score : {self.score}", align=ALIGN, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()