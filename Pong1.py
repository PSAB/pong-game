# import turtle graphics module
import turtle

# Create window instance
wn = turtle.Screen()
wn.title('Pong by Pavan Sabnis') # window title
wn.bgcolor("black") # background color
wn.setup(width=800, height=600) # window size
wn.tracer(0) # stops window from updating for faster performace


# Paddle A
paddle_a = turtle.Turtle() # paddle a is a turtle object
paddle_a.speed(0) # sets turtle speed to maximum possible
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Paddle shape: Default is 20x20 px, now its 100x20 px because of stretch
paddle_a.penup() # 'pull the pen up' AKA no drawing during turtle movement
paddle_a.goto(-350,0) # Moves turtle to specified position. Line is drawn if pen is down


# Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup() 
paddle_b.goto(350,0) # Modify specified position to be on the right side


# Ball
ball = turtle.Turtle() 
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup() 
ball.goto(0,0) # Modify specified position to be on the right side
ball.dx = 3.5 # These are the ball position increment speeds for its movement
ball.dy = 3.5

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    if y > 260:
        y = -240
    else:
        y += 30
    # print(y)
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y < -240:
        y = 260
    else:
        y -= 30
    # print(y)
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    if y > 260:
        y = -240
    else:
        y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y < -240:
        y = 260
    else:
        y -= 30
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # Listen for keyboard input
wn.onkeypress(paddle_a_up, 'w') # When user presses w, call paddle_a_up
wn.onkeypress(paddle_a_down, 's') # When user presses s, call paddle_a_down
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for y:
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    # Border checking for x:
    if ball.xcor() > 380:
        ball.setx(380)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    # Ball and paddle collisions:
    # Paddle b:
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340) # if ball ends up behind paddle, put it in front right away to prevent getting stuck
        ball.dx *= -1
    # Paddle a:
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340) # if ball ends up behind paddle, put it in front right away to prevent getting stuck
        ball.dx *= -1