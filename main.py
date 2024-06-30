import time
from turtle import *
from paddle import Paddle
from ball import Ball
from score import Score

score = Score()
ball = Ball()
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG GAME')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
game_is_on = True

while game_is_on:
    time.sleep(ball.speed_move)
    screen.update()
    ball.move()

    if ball.ycor() > 289 or ball.ycor() < -300:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        # score.inc_score()
        # score.inc_score()

    if ball.xcor() > 370 :
        ball.reset_ball()
        score.l_point()

    if  ball.xcor() < -370:
        ball.reset_ball()
        score.r_point()
screen.exitonclick()
