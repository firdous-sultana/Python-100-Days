# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random
guess = random.randint(0, 1)
if(guess == 0):
	print("Tail")
else:
	print("Head")