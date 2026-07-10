
# Blind Auction

This is a simple **Blind Auction** program written in Python.

The application collects bids from multiple participants, stores them in a dictionary, and determines the highest bid once all users have entered their offers. If multiple participants submit the same highest bid, the program announces a tie.

## Flowchart

```text
                     Start
                       │
                       ▼
                 Display Logo
                       │
                       ▼
            Enter Name and Bid
                       │
                       ▼
             Store Bid in Dictionary
                       │
                       ▼
             More Participants?
                 ┌─────┴─────┐
                 │           │
               Yes          No
                 │           │
                 ▼           ▼
          Clear Screen   Find Highest Bid
                 │           │
                 │           ▼
                 │      Tie Detected?
                 │      ┌────┴────┐
                 │      │         │
                 │     Yes       No
                 │      │         │
                 │      ▼         ▼
                 │  Display Tie  Display Winner
                 │
                 └───────────────►
                                 │
                                 ▼
                                End
```

## Features

- Collects bids from multiple users
- Stores bids in a Python dictionary
- Finds the highest bid automatically
- Detects ties between bidders
- Simple command-line interface
- Uses loops, dictionaries, and conditional statements

## Project Structure

```text
.
├── art.py
├── Blind_Auction_Project.py
└── README.md
```

## How to Run

```bash
python Blind_Auction_Project.py
```

## Example

```text
What is your name?
Alice

What is your bid?
100

Are there other users who want to bid?
yes

What is your name?
Bob

What is your bid?
150

Are there other users who want to bid?
no

The winner is Bob with a bid of $150.
```

## Concepts Practiced

- Dictionaries
- Loops (`while`, `for`)
- Conditional statements (`if`, `elif`, `else`)
- User input
- Lists
- Finding the maximum value
- Program flow control
