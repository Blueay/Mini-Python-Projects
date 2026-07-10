
# Higher Lower Game Project

This is a simple **Higher Lower** game written in Python.

The objective is to guess which person, brand, or organization has **more Instagram followers**. For every correct guess, your score increases and the winning account advances to the next round. The game continues until you make an incorrect guess.

Inspired by the online game:

http://www.higherlowergame.com

## Flowchart

```text
                     Start
                       │
                       ▼
                 Display Logo
                       │
                       ▼
          Select Two Random Accounts
                       │
                       ▼
         Display Account A and B
                       │
                       ▼
              Player Makes Guess
                  (A or B)
                       │
                       ▼
          Compare Follower Counts
                       │
                 ┌─────┴─────┐
                 │           │
              Correct      Wrong
                 │           │
                 ▼           ▼
           Increase Score  Show Final Score
                 │           │
                 ▼           ▼
     Move B → A and Pick New B
                 │           │
                 └─────┬─────┘
                       │
                       ▼
                    Repeat
```

## Features

- Randomly selects Instagram accounts
- Compares follower counts
- Tracks the player's score
- Winner advances to the next round
- Prevents duplicate comparisons
- Simple command-line interface

## Project Structure

```text
.
├── art.py
├── game_data.py
├── HigherLower_Project.py
└── README.md
```

## How to Run

```bash
python HigherLower_Project.py
```

## Example

```text
Compare A:
Instagram, a Social media platform, from United States

VS

Against B:
Cristiano Ronaldo, a Footballer, from Portugal

Who has more followers?
Type 'A' or 'B':
A

Correct! You got it right.
Current score: 1
```

## Concepts Practiced

- Functions
- Lists
- Dictionaries
- Nested data structures
- Random module
- Loops (`while`)
- Conditional statements (`if`, `else`)
- User input
- String formatting (f-strings)
- Boolean logic
- Program flow control
- Game state management

## Further Reading

### Original Higher Lower Game

Play the original browser game:

http://www.higherlowergame.com
