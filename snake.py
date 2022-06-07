from turtle import Turtle

STARTING_POS = [(0, 0), (-10, 0), (-20, 0)]
MOVING_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.dots = []
        self.create_snake()
        self.head = self.dots[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_dot(pos)

    def add_dot(self, pos):
        new_dot = Turtle("square")
        new_dot.color("white")
        new_dot.penup()
        new_dot.shapesize(.5, .5)
        new_dot.goto(pos)
        self.dots.append(new_dot)

    def extend(self):
        self.add_dot(self.dots[-1].position())

    def reset(self):
        for dot in self.dots:
            dot.goto(1000, 1000)
        self.dots.clear()
        self.create_snake()
        self.head = self.dots[0]

    def move(self):
        # loop in range start=2 -> 1 -> stop=0, step = -1
        for dot in range(len(self.dots) - 1, 0, -1):
            new_x = self.dots[dot - 1].xcor()    # pos x of 1
            new_y = self.dots[dot - 1].ycor()    # pos y of 1
            self.dots[dot].goto(new_x, new_y)    # move 2 -> 1

        self.head.forward(MOVING_DISTANCE)  # move the head

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
