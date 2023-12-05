from turtle import Screen,Turtle
from paddle import paddle
from ball import ball
from score import score
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
r_paddle=paddle((350,0))
l_paddle=paddle((-350,0))
ball_=ball()
scores=score()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game=True
while game:
    time.sleep(ball_.movespeed)
    screen.update()
    ball_.move()
    if ball_.ycor()>280 or ball_.ycor()<-280:
        ball_.bounce_y()
    if ball_.distance(r_paddle)<50 and ball_.xcor()>320 or ball_.distance(l_paddle)<50 and ball_.xcor()<-320:
        ball_.bounce_x()    
    if ball_.xcor()>380:
        scores.l_point()
        ball_.ball_reset()
        scores.update_score()
    if ball_.xcor()<-380:
        ball_.ball_reset()
        scores.r_point()
        scores.update_score()
screen.exitonclick()