print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn = input("You are on a crossroad! Where would you like to go? Enter 'left' or 'right'").lower()
# lake = input("You have come to a lake! There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.").lower()
# wait = input("The island has 3 doors. Enter the door color: 'red', 'blue' or 'yellow'?").lower()

if (turn == 'left'):
    lake = input("You have come to a lake! There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.").lower()
    if(lake == 'wait'):
        door = input("The island has 3 doors. Enter the door color: 'red', 'blue' or 'yellow'?").lower()
        if(door == 'red'):
            print("Burned by fire. Game over.")
        elif(door == 'blue'):
            print("Eaten by beasts. Game over.")
        elif(door == 'yellow'):
            print("You win.")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game over.")