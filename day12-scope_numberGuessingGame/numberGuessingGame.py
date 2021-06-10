#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

def set_difficulty(level):
    if level == 'easy':
        calculate_guess(10)
    elif level == 'hard':
        calculate_guess(5)
    else:
        print("Invalid level!")

def calculate_guess(rounds):
    my_guess = random.randint(1, 100)
    # print("Psst, the solution is {}".format(my_guess))
    while rounds > 0:
        print("You have {} attempts remaining to guess a number.".format(rounds))
        user_guess = int(input("Make a guess. "))
        if(user_guess < my_guess):
            print("Too low.")
        elif(user_guess > my_guess):
            print("Too high.")
        else:
            print("Win win Correct Guess ;)")
            break
        print("Guess again.")
        rounds -= 1
    if rounds == 0:
        print("You've ran out of guesses. You lose.")
        


print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard'").lower()

set_difficulty(level)
