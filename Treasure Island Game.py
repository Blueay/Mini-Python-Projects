print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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


crossroad = input("you are at the crossroad. Where do you want to go? Type 'left' or 'right'.\n").lower()
if crossroad == "left" or crossroad == "Left":
    print("You crossed the treasure path.")
else:
    print("You fall into a hole. Game Over")

lake = input("You reach a beautiful lake with crystal water. Do you want to 'swim' or 'wait'?\n").lower()
if lake == "wait":
    print("You discover at the end of the lake a bridge which leads to the castle")
else:
    print(" You are attached by a trout. Game Over")

door = input("You enter the castle and in front of you are 3 big doors in the color 'red', 'green' and 'blue'. Which one do you choose?\n").lower()
if door == "red": print("Behind the door ther is a fire and you escape. Game Over")
if door == "blue": print("You get eaten by a beast. Game Over")
if door == "green": print("You Win!")
else: print("Game Over.Start from New!")

