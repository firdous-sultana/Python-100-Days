# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
names_index = random.randint(0, len(names)-1)
print(names[names_index] + " is going to buy the meal today!")