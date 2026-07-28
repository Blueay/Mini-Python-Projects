
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
game_images = [rock, paper, scissors]

your_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))
if your_choice >=0 and your_choice <=2:
    print(f"You chose:")
    print(game_images[your_choice])

random_choice = random.randint(0,2)
print(f"Computer chose:")
print(game_images[random_choice])



if your_choice >=3 or your_choice <0:
    print("You typed a wrong number. You lose!")
elif your_choice == random_choice:
    print("It is a draw!")
elif your_choice == 0 and random_choice == 2:
    print("You win!")
elif your_choice == 2 and random_choice == 0:
    print("You lose!")
elif random_choice > your_choice:
    print("You lose!")
elif your_choice > random_choice:
    print("You win!")

