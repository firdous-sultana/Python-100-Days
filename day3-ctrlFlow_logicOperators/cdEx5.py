# write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2

lower_name = combined_string.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")

true_sum = t + r + u + e
love_sum = l + o + v + e

love_score = true_sum * 10 + love_sum

if love_score<10 or love_score>90:
	print("Your score is " + str(love_score) + ", you go together like coke and mentos.")
elif love_score>40 and love_score<50:
	print("Your score is " + str(love_score) + ", you are alright together.")
else:
	print("Your score is " + str(love_score) + ".")