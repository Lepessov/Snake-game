import time

from turtle import Turtle, Screen
from snake import Snake
from score import ScoreBoard
from food import Food

screen = Screen()
score = ScoreBoard()
food = Food()
snake = Snake()

screen.setup(width=600, height=600)
screen.title('My snake game')
screen.bgcolor('white')
screen.tracer(0)


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game = True

while game:
    screen.update()
    time.sleep(0.09)
    snake.move()


    # Detecting collision with a food
    if snake.head.distance(food) < 15:
        food.move()
        score.add()
        score.update()
        snake.extend()
    
    # Detecting collision with a wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detecting collision with a tail
    for snake_body in snake.snake_bodies[1:]:

        if snake.head.distance(snake_body) < 10:
            score.reset()
            snake.reset()



















screen.exitonclick()
















screen.exitonclick()
