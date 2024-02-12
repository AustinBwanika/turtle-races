from turtle import Turtle, Screen
import random

tim1 = Turtle(shape="turtle")
tim2 = Turtle(shape="turtle")
tim3 = Turtle(shape="turtle")
tim4 = Turtle(shape="turtle")
tim5 = Turtle(shape="turtle")
tim6 = Turtle(shape="turtle")
should_continue = True
winning_turtle = ""
turtles = [tim1, tim2, tim3, tim4, tim5, tim6]


screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(0, len(colors)):
    temp = colors[i]
    turtles[i].color(temp)
    turtles[i].penup()


screen.setup(width=500, height=400)


bet = screen.textinput(title="Austin Betting Palace", prompt = "Which colour turtle will win the race:".lower())
tim1.goto(x=-230, y=0)
tim2.goto(x=-230, y=50)
tim3.goto(x=-230, y=-50)
tim4.goto(x=-230, y=100)
tim5.goto(x=-230, y=-100)
tim6.goto(x=-230, y=150)

while should_continue:
    for i in range(0, len(turtles)):
        turtles[i].forward(random.randint(5, 25))
        if turtles[i].xcor() > 250 - (40/2):
            should_continue = False
            winning_turtle = colors[i]

if winning_turtle == bet:
    print(f"Congratulations. {winning_turtle} won. You have gained money!")
else:
    print(f"You lose. {winning_turtle} won the race")

screen.exitonclick()
