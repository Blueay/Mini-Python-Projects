# Blackjack

This is a simple **Blackjack** game written in Python.

The game follows the basic rules of Blackjack, where the player competes against the computer. Both players are dealt cards from a virtual deck, and the objective is to get as close to **21** as possible without going over. The computer follows the standard Blackjack rule of drawing cards until it reaches a score of at least **17**.

## Flowchart

```text
                    Start
                      │
                      ▼
                 Display Logo
                      │
                      ▼
           Deal Two Cards Each
                      │
                      ▼
            Calculate Scores
                      │
                      ▼
            Blackjack or Bust?
                 ┌────┴────┐
                 │         │
               Yes        No
                 │         │
                 ▼         ▼
           End Player Turn  Hit or Stand?
                              ┌────┴────┐
                              │         │
                            Hit      Stand
                              │         │
                              ▼         ▼
                       Draw New Card   Dealer's Turn
                              │         │
                              └────┬────┘
                                   ▼
                      Dealer Draws Until 17+
                                   │
                                   ▼
                          Compare Scores
                                   │
                                   ▼
                           Display Winner
                                   │
                                   ▼
                          Play Again?
                              ┌───┴───┐
                              │       │
                            Yes      No
                              │       │
                              ▼       ▼
                           Restart    End
```

## Features

- Play against the computer
- Random card dealing
- Automatic Blackjack detection
- Ace value automatically changes from **11** to **1** when necessary
- Dealer follows the Blackjack rule of drawing until reaching **17**
- Continue playing multiple rounds without restarting the program

## Project Structure

```text
.
├── art.py
├── The_Blackjack_Project.py
└── README.md
```

## How to Run

```bash
python The_Blackjack_Project.py
```

## Example

```text
Do you want to play a game of Blackjack? Type 'y' or 'n':
y

Your cards: [10, 7], current score: 17
Computer's first card: 9

Type 'y' to get another card or 'n' to pass:
n

Your final hand: [10, 7], final score: 17
Computer's final hand: [9, 8], final score: 17

Draw 🙃
```

## Concepts Practiced

- Functions
- Lists
- List methods (`append()`, `remove()`)
- Loops (`while`, `for`)
- Conditional statements (`if`, `elif`, `else`)
- Random module
- User input
- Return values
- The built-in `sum()` function
- Program flow control
- Game logic

## Further Reading

- **Python Lists (Google for Education)**
  https://developers.google.com/edu/python/lists#for-and-in

- **Python List Methods (Google for Education)**
  https://developers.google.com/edu/python/lists#list-methods

- **Python Built-in `sum()` Function**
  https://docs.python.org/3/library/functions.html#sum
