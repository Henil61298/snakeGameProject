from turtle import Screen, Turtle
from snake import Snake
from scoreboard import Scoreboard
from Food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     detect collision

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

#     If head collides with any other segments
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()






















screen.exitonclick()
