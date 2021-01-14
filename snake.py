import time
from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-40, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create a snake body by creating three connected squares"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # the two functions above are what creates the snake

    def extend(self):
        """Adds a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move snake continuously move forward, so all we need to do is tell it to change direction"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # self.snake.up(100)

    def down(self):
        # pass
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # pass
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # pass
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
