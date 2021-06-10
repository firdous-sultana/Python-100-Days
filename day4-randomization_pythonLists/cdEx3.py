# You are going to write a program which will mark a spot with an X

# 🚨 Don't change the code below 👇
row1 = ["0","0","0"]
row2 = ["0","0","0"]
row3 = ["0","0","0"]
map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
print("{}\n{}\n{}".format(row1, row2, row3))
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# horizontal = int(position[0])
# vertical = int(position[1])	

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = 'X'

# map[vertical - 1][horizontal - 1] = 'X'

map[int(position[1]) - 1][int(position[0]) - 1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
print("{}\n{}\n{}".format(row1, row2, row3))