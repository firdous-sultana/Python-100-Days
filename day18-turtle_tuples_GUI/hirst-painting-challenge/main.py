# import colorgram

# rgb_colors = []
# colors = colorgram.extract('spot_paint.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)


import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()
color_list = [(21, 114, 173), (142, 163, 184), (204, 137, 166), (190, 173, 17), (145, 17, 32), (238, 213, 62), (67, 24, 31), (17, 138, 59), (219, 161, 88), (122, 71, 100), (49, 29, 26), (197, 65, 28), (7, 107, 64), (227, 169, 197), (240, 78, 29), (29, 177, 84), (21, 172, 188), (243, 214, 4), (110, 192, 140), (182, 94, 115), (35, 37, 46), (188, 182, 213), (157, 206, 215), (240, 168, 154), (147, 215, 171), (127, 32, 26)]
tim.speed('fastest')


tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = t.Screen()
screen.exitonclick()