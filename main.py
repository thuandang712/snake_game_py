import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
# Turn off tracer
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


# control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)  # slow the snake down
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset()

    # detec collision with tail
    # if head collides with any dots in the tail -> game over
    for dot in snake.dots[1:]:
        if snake.head.distance(dot) < 8:
            scoreboard.reset_score()
            snake.reset()


screen.exitonclick()
