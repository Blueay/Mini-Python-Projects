import art
from random import randint

# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
print(art.logo2)

# guess_number = int(random.choice(range(1,101)))
guess_number = randint(1, 100)


# print(guess_number)


def easy_game():
    attempts = 10
    # Repeat the guessing functionality if they get it wrong.
    while attempts > 0:
        # Let the user guess a number
        user_guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))

        """Checks answer against guess, returns the number of turns remaining."""
        if user_guess == guess_number:
            print("You guessed the number! You win.")
            break
        elif user_guess < guess_number:
            attempts -= 1
            print("Too low.")
        else:
            attempts -= 1
            print("Too high.")

    if attempts == 0:
        print(f"You ran out of tries! The number was {guess_number}.")


def hard_game():
    attempts = 5
    # Repeat the guessing functionality if they get it wrong.
    # Track the number of turns and reduce by 1 if they get it wrong
    while attempts > 0:
        # Let the user guess a number
        user_guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))

        """Checks answer against guess, returns the number of turns remaining."""
        if user_guess == guess_number:
            print("You guessed the number! You win.")
            break
        elif user_guess < guess_number:
            attempts -= 1
            print("Too low.")
        else:
            attempts -= 1
            print("Too high.")

    # No attempts left
    if attempts == 0:
        print(f"You ran out of tries! The number was {guess_number}.")


# Choosing a random number between 1 and 100.
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Function to set difficulty
level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
if level == "easy":
    easy_game()
elif level == "hard":
    hard_game()
else:
    print("you typed a wrong word. Run again.")
