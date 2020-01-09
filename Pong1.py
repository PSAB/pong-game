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
paddle_b.goto(350,0) 


# Ball


# Main game loop
while True:
    wn.update()

