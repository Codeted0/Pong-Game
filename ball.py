from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_move = 0.09
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1
        self.speed_move *= 0.9
    def bounce_x(self):
        self.x_move *= -1


    def reset_ball(self):
        self.speed_move = 0.1
        self.goto(0, 0)
        self.bounce_x()
