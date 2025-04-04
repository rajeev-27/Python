from turtle import Screen
from snake import Snake
from food import  Food
from scoreboard import Score
import time

screen =Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on =True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food)<12:
        food.refresh()
        score.increase_point()

screen.exitonclick()