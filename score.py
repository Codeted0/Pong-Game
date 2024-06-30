from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.goto(100, 200)
        self.write(arg=f'{self.r_score}', align='center', font=('Arial', 50, 'normal'))
        self.goto(-100, 200)
        self.write(arg=f'{self.l_score}', align='center', font=('Arial', 50, 'normal'))
    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()
    def l_point(self):
        self.l_score +=1
        self.clear()
        self.update_score()