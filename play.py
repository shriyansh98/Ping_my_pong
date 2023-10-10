from turtle import Screen 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()

STARTING_POSITION_1 = (370,0)
STARTING_POSITION_2 = (-370,0)
 



def pin_pong():
    
    playing = True

    screen.setup(width=800 ,height=600)
    screen.bgcolor("black")
    screen.title("Ping my Pong")
    screen.tracer(0)
  
    r_paddle = Paddle(STARTING_POSITION_1)
    l_paddle = Paddle(STARTING_POSITION_2)

    ball = Ball() 
    scoreboard = Scoreboard()

    screen.listen()

    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down,"Down")

    screen.onkey(l_paddle.up,"w")
    screen.onkey(l_paddle.down,"s")
 


    while playing:
        time.sleep(ball.ball_speed)
        screen.update()
        ball.move()

        if ball.ycor()> 280 or ball.ycor()< -280:
            ball.bounce()

        
        if ball.distance(r_paddle)<50 and ball.xcor() >340: 
        # or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
            ball.hit()

        if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
            ball.hit()


        if ball.xcor() > 380:
            
            ball.miss()
            scoreboard.r_point()
            

        if ball.xcor() < -380:
            
            ball.miss()
            scoreboard.l_point()
            
pin_pong()
screen.exitonclick()