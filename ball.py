from turtle import Turtle
class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x=10
        self.y=10
        self.movespeed=0.1
    def move(self):
        x=self.xcor()+self.x
        y=self.ycor()+self.y
        self.goto(x,y)
    def bounce_y(self):
        self.y*=-1
    def bounce_x(self):
        self.x*=-1
        self.movespeed*=0.9
    def ball_reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.movespeed=0.1
        
        
    
        
        