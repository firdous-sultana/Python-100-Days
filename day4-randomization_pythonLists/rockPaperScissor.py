rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

print("Welcome to the Rock Paper Scissors game!")
choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))

random_choice = random.randint(0, 2)

#Winning side
if(choice == 0):
    print(rock)
    if(random_choice == 0):
        print("Computer chose:" + rock + "\nDraw")
    if(random_choice == 1):
        print("Computer chose:" + paper + "\nYou lose")
    if(random_choice == 2):
        print("Computer chose:" + scissors + "\nYou win")
elif(choice == 1):
    print(paper)
    if(random_choice == 0):
        print("Computer chose:" + rock + "\nYou win")
    if(random_choice == 1):
        print("Computer chose:" + paper + "\nDraw")
    if(random_choice == 2):
        print("Computer chose:" + scissors + "\nYou lose")
else:
    print(scissors)
    if(random_choice == 0):
        print("Computer chose:" + rock + "\nYou lose")
    if(random_choice == 1):
        print("Computer chose:" + paper + "\nYou win")
    if(random_choice == 2):
        print("Computer chose:" + scissors + "\nDraw")