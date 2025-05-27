import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make ur bet", prompt="Which turtle do you want to win a race? Enter a color:")
colors = ["red", "blue", "green", "yellow", "purple", "pink", "white"]
y_position= [-70,-40,-10,20,50,80]
all_turtles = []
print(user_bet)

for turtle in range(0,6):

  new_turtle = Turtle(shape="turtle")
  new_turtle.color(colors[turtle])
  new_turtle.penup()
  new_turtle.goto(x=-250, y=y_position[turtle])
  all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! the {winning_color} turtle is the winner!")
            else:
                print(f"You Lose the {winning_color} turtle is the winner!")

            print(turtle.color())

        random_distance=  random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()

'''
def move_fowards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_fowards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
clear()

screen.mainloop()  # Add this to keep the window open
'''