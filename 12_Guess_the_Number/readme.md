
# Guess the Number

This is a simple **Guess the Number** game written in Python.

The program randomly selects a number between **1 and 100**, and the player tries to guess it within a limited number of attempts. Two difficulty levels are available:

- **Easy:** 10 attempts
- **Hard:** 5 attempts

After each guess, the game provides feedback indicating whether the guess was **too high** or **too low** until the player wins or runs out of attempts.

## Flowchart

```text
                    Start
                      │
                      ▼
                Display Logo
                      │
                      ▼
         Generate Random Number
             (between 1–100)
                      │
                      ▼
          Choose Difficulty
          (Easy or Hard)
                      │
                      ▼
            Set Attempts
                      │
                      ▼
             Enter Guess
                      │
                      ▼
            Correct Guess?
             ┌────┴────┐
             │         │
           Yes        No
             │         │
             ▼         ▼
       Display Win   Too High/Low
                         │
                         ▼
                Attempts Left?
                   ┌────┴────┐
                   │         │
                 Yes        No
                   │         │
                   ▼         ▼
             Guess Again   Reveal Number
                              │
                              ▼
                             End
```

## Features

- Random number generation
- Two difficulty levels
- Hint system ("Too high" / "Too low")
- Limited number of attempts
- Simple command-line interface
- Beginner-friendly game logic

## Project Structure

```text
.
├── art.py
├── Guess_the_Number_Project.py
└── README.md
```

## How to Run

```bash
python Guess_the_Number_Project.py
```

## Example

```text
Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.

Choose a difficulty level.
Type 'easy' or 'hard':
hard

You have 5 attempts remaining to guess the number.
Make a guess:
50

Too low.

You have 4 attempts remaining to guess the number.
Make a guess:
75

Too high.
```

## Concepts Practiced

- Functions
- Variables
- Loops (`while`)
- Conditional statements (`if`, `elif`, `else`)
- Random number generation
- User input
- Program flow control
- Game logic
- Function decomposition

## Further Reading

### ASCII Art Generator

Create custom ASCII banners like the one used in this project:

http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false

### Python Tutor

Step through your Python code line by line and visualize how variables change during execution:

https://pythontutor.com/visualize.html#mode=edit
