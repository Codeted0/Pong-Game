from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        # self.color('red')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.create_paddles(position)

    def create_paddles(self, position):
        self.goto(position)
        if position == (350, 0):
            self.color('DodgerBlue')
        else :
            self.color('Magenta')
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
