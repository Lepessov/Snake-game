import random


from turtle import Turtle

STARTING_POSITIONS = ((0,0), (-20, 0), (-40,0))
UP = 90 
DOWN = 270 
LEFT =  180 
RIGHT = 0 
DISTANCE = 20
COLORS = ('red', 'yellow', 'orange', 'purple') 

class Snake():

    
    def __init__(self):
        self.snake_bodies = []
        self.create_snake()
        self.head = self.snake_bodies[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_body = Turtle()
            snake_body.shape('square')
            snake_body.color(random.choice(COLORS))
            snake_body.penup()
            snake_body.goto(position)
            self.snake_bodies.append(snake_body)

    def reset(self):
        for sb in self.snake_bodies:
            sb.goto(1000, 1000)
        self.snake_bodies.clear()
        self.create_snake()
        self.head = self.snake_bodies[0]


    def extend(self):
        tail = self.snake_bodies[-1]
        snake_body = Turtle()
        snake_body.shape('square')
        snake_body.color(random.choice(COLORS))
        snake_body.penup()
        snake_body.goto(tail.xcor(), tail.ycor())
        self.snake_bodies.append(snake_body)

    def move(self):
        for i in range(len(self.snake_bodies) - 1, RIGHT, -1):
                new_x = self.snake_bodies[i - 1].xcor()
                new_y = self.snake_bodies[i - 1].ycor()
        
                self.snake_bodies[i].goto(new_x, new_y)
        
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

