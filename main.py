from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race , enter the color: ")

colors = ["red", "yellow", "orange", "blue", "violet", "green"]
y_position = [-100, -50, 0, 50, 100, 150]
all_turtles = []
race_is_on = False

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.goto(230, 180)
tim.setheading(270)
while tim.ycor() > -150:
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
tim.hideturtle()


for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True


while race_is_on:
    for turtle in all_turtles:
        pace = random.randint(1, 10)
        turtle.forward(pace)
        if turtle.xcor() > 230:
            race_is_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"you won ! The wining turtle is actually {wining_color}")
            else:
                print(f"you lost , the wining turtle is {wining_color}")

screen.exitonclick()