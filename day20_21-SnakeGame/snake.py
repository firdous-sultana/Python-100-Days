from turtle import Turtle
STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
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
        for position in STARTING_POSITIONS:
            sn = Turtle("square")
            sn.color("white")
            sn.penup()
            sn.goto(position)
            self.segments.append(sn)
    
    def move(self):
        for seg_number in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # self.segments[0].setheading(90)
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






# Make Snake



# Move snake

# We don't just move forward as whole, as the turnings won't be done the same way as for all 3 turtles
    # for seg in segments:
    #     seg.forward(20)
    # A good solution is to start the movement from last block

    # for seg_number in range(start=2, stop=0, step=-1):
    