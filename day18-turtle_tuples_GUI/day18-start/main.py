from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("coral2")

# # Square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)



# # Dashed line
# for _ in range(10):
# 	tim.forward(10)
# 	tim.penup()
# 	tim.forward(10)
# 	tim.pendown()


# # Triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon : overlayed; drawn in sequence; size = 100
# colors = ["indian red", "burlywood", "goldenrod", "medium orchid", "maroon", "medium blue", "alice blue", "gold"]

# def draw_shape(num_sides):
# 	angle = 360/num_sides
# 	for sides in range(num_sides):
# 		tim.forward(100)
# 		tim.right(angle)

# for _ in range(3, 11):
# 	tim.color(random.choice(colors))
# 	draw_shape(_)

# Draw a random walk
colors = ["indian red", "burlywood", "goldenrod", "medium orchid", "maroon", "medium blue", "alice blue", "gold"]
directions = [0, 90, 180, 270]
tim.pensize(width = 15)

for _ in range(200):
	tim.color(random.choice(colors))
	tim.forward(30)
	tim.setheading(random.choice(directions))

tim.speed('fastest')


screen = Screen()
screen.exitonclick()