from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-350,400)
        self.write(f"Level {self.level}", font=FONT)
        
    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!",align="center", font=("Courier", 24, "bold"))