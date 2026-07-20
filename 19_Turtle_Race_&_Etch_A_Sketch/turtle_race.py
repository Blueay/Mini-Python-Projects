import turtle
from turtle import Turtle, Screen
import random
from tkinter import messagebox


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet:", prompt= "Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
print(user_bet)
print(all_turtles)

is_race_on = False

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
    #the finish line is x.coordinate = 230 (is 250 - half the width of the turtle 20)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                #print(f"You win! The {winning_color} turtle is the winner 🐢")
                messagebox.showinfo(
                     "Race Result",
                     f"You win! The {winning_color} turtle is the winner 🐢"
                )


            else:
                #print(f"You have lost! The {winning_color} turtle is the winner 🐢")
                messagebox.showinfo(
                     "Race Result",
                     f"You have lost! \n The {winning_color} turtle is the winner 🐢"
                )



        #Make each turtle move a random amount
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
