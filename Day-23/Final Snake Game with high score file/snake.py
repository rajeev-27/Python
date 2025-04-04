from turtle import Turtle

INDEX = [(0, 0),(-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in INDEX:
            self.increase_size(i)

    def increase_size(self, i):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(i)
        self.segment.append(tim)

    def extend_snake(self):
        self.increase_size(self.segment[-1].position())

    def move(self):
        for z in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[z - 1].xcor()
            new_y = self.segment[z - 1].ycor()
            self.segment[z].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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

    def reset_snake(self):
        for seg  in self.segment:
            seg.goto(1000, 10000)
        self.segment.clear()
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]