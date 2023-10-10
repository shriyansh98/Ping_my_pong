from turtle import Turtle
MOVE_D = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = MOVE_D 
        self.move_y = MOVE_D
        self.ball_speed = 0.1
    
    
     
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y

        self.goto(new_x,new_y) 

    def bounce(self):
            self.move_y *= -1
            self.ball_speed * 0.075
            print(self.ball_speed)

    def hit(self):
         self.move_x *= -1
         self.ball_speed * 0.05
         print(self.ball_speed)


    def miss(self):
        self.goto(0,0)
        self.move_x *= -1


        



