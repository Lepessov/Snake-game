from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 25, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hscore = 0
        self.ht()
        self.penup()
        self.goto(0, 250)
        self.update()
        

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)


    def update(self):
        self.write(f'Score: {self.score} Highscore: {self.hscore}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score >= self.hscore:
            self.hscore = self.score
        self.score = 0
        self.clear()
        self.update()


    def add(self):
        self.clear()
        self.score = self.score + 1
        
