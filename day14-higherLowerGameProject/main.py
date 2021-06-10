import random
import art
from game_data import data

# Clear screen function
import os
clear = lambda: os.system('cls')

def format_data(account):
    '''Format the account data into printable format'''
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return ("{}, a {}, from {}".format(account_name, account_descr, account_country))

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right.
  Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# print the art
print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:

    # Making account at position B become the next account at position A.
    # Generate random account from game data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    # print(account_a)
    # print(account_b)


    print("Compare A: " + format_data(account_a))
    print(art.vs)
    print("Compare B: " + format_data(account_b))

    # Ask user for a guess
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    fcount_a = account_a['follower_count']
    fcount_b = account_b['follower_count']
    # is_correct = check_answer(choice, fcount_a, fcount_b)

    # Clear screen between rounds.
    clear()
    print(art.logo)

    # Give user feedback on their guess.
    if check_answer(choice, fcount_a, fcount_b):
        # Score
        score += 1
        print("You're right! Current score: {}".format(score))
    else:
        game_should_continue = False
        print("Sorry! That's wrong. Final score: {}".format(score))







