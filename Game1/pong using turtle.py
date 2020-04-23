import turtle
import time
import os
# some constats
audiopath=r'/home/shikari/games-using-python/Game1/Spring-Boing.mp3'
timedelay=0.01
# setting up our window
root=turtle.Screen()
root.setup(width=800,height=600)
root.title("Play Pong by Rahul")
root.bgcolor("black")
root.tracer(0)

start=False
# welcome screen

pen=turtle.Turtle()
pen.speed(0)
pen.color("Yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,0)

def startgame():
    global start
    start=True
    

while(not start):    
    pen.write("Welcome to classic pong! Press S to start", align='center',font=("courier",24,"normal"))
    root.listen()
    root.onkeypress(startgame ,'s')     

pen.clear()


# Score
score1=0
score2=0


# 1st paddle
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.color("orange")
paddle1.penup()
paddle1.goto(-350,0)

# 2nd paddle
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.color("orange")
paddle2.penup()
paddle2.goto(350,0)

# Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2


# Pen

pen.color("white")

pen.goto(0,260)
pen.write("Player A: {}  Player B: {}".format(score1,score2), align='center',font=("courier",24,"normal"))



# Some functions
def paddle1_up():
    y=paddle1.ycor()
    y+=20
    paddle1.sety(y)
def paddle1_down():
    y=paddle1.ycor()
    y-=20
    paddle1.sety(y)
def paddle2_up():
    y=paddle2.ycor()
    y+=20
    paddle2.sety(y)
def paddle2_down():
    y=paddle2.ycor()
    y-=20
    paddle2.sety(y)


# Binding Keys
root.listen()
root.onkeypress(paddle1_up,'q') 
root.onkeypress(paddle1_down,'a') 
root.onkeypress(paddle2_up,'Up') 
root.onkeypress(paddle2_down,'Down') 




#  main game loop
while True:
    root.update()  

    # moving ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    time.sleep(timedelay)

    # border checking and bouncing back
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        ball.dy*=-1
        score1+=1
        os.system("ffplay -nodisp -autoexit {}&".format(audiopath))
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1,score2), align='center',font=("courier",24,"normal"))
        time.sleep(1)
        

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score2+=1
        os.system("ffplay -nodisp -autoexit {}&".format(audiopath))
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1,score2), align='center',font=("courier",24,"normal"))
        ball.goto(0,0)
        time.sleep(1)

        
    # bouncing with the paddle
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()>paddle1.ycor()-45 and ball.ycor()<paddle1.ycor()+45):
        ball.dx*=-1
        ball.setx(-340)
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()>paddle2.ycor()-45 and ball.ycor()<paddle2.ycor()+45):
        ball.dx*=-1 
        ball.setx(340)

    # changing game speed
    if (score1>=5 and score1<10) or (score2>4 and score2<10):
        timedelay=0.007
    if (score1>=10 and score1<15) or (score2>9 and score2<15):
        timedelay=0.006
    if (score1>=15 and score1<20) or (score2>14 and score2<20):
        timedelay=0.005
    
 