from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pensize(5)
screen.setup(width=800, height=600)



def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(30)

def turn_right():
    tim.right(30)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="q", fun=clear)

screen.exitonclick()


