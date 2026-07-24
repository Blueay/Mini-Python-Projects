# 🇺🇸 U.S. States Game

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-success)
![CSV](https://img.shields.io/badge/Data-CSV-orange)
![Turtle](https://img.shields.io/badge/GUI-Turtle_Graphics-green)

An interactive geography quiz built with **Python**, **Pandas**, **CSV files**, and **Turtle Graphics**.

The goal of the game is to correctly name all **50 U.S. states**. Every correct answer is displayed at its corresponding location on the map. If the player exits the game before completing all states, the program automatically creates a CSV file containing the missing states for future learning.

---

## Screenshot

<p align="center">
  <img src="blank_states_img.gif" width="750" alt="U.S. States Game">
</p>

---

## Features

- 🇺🇸 Interactive U.S. map
- 📍 Displays correctly guessed states on the map
- 📊 Uses a CSV dataset containing all 50 states
- 🐼 Reads and filters data with Pandas
- 💾 Automatically generates a `states_to_learn.csv` file
- 🎯 Tracks the player's progress
- 🖥 Beginner-friendly graphical interface using Turtle Graphics

---

## Flowchart

```text
                    Start
                      │
                      ▼
             Load CSV Dataset
                      │
                      ▼
            Display U.S. Map
                      │
                      ▼
             Ask for State Name
                      │
          ┌───────────┼────────────┐
          │           │            │
          ▼           ▼            ▼
      Correct?      Exit?      Wrong?
          │           │            │
         Yes         Yes          No
          │           │            │
          ▼           ▼            │
 Display State   Save Missing      │
 On Map          States to CSV     │
          │           │            │
          └──────┬────┴────────────┘
                 ▼
          All States Found?
              ┌────┴────┐
              │         │
             No        Yes
              │         │
              ▼         ▼
         Continue    Congratulations!
```

---

## Project Structure

```text
US-States-Game/
│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
├── README.md
└── images/
    └── us_states_game.png
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/us-states-game.git
```

Navigate into the project folder:

```bash
cd us-states-game
```

Run the application:

```bash
python main.py
```

---

## Gameplay

1. Start the game.
2. Enter the name of a U.S. state.
3. Every correct answer appears on the map.
4. Continue until all 50 states have been guessed.
5. Type **Exit** at any time to finish the game.
6. A new file named **states_to_learn.csv** is generated containing all states that were not guessed.

---

## Concepts Practiced

### Python

- Loops
- Lists
- Conditional statements
- User input
- String manipulation

### Pandas

- Reading CSV files
- DataFrames
- Filtering rows
- Exporting DataFrames to CSV

### Turtle Graphics

- Custom background images
- Writing text on the screen
- Coordinates
- Turtle objects

### Data Processing

- CSV datasets
- Data filtering
- Data persistence
- Generating new datasets

---

## Further Reading

### Pandas Documentation

https://pandas.pydata.org/docs/reference/index.html

### Python Turtle Graphics

https://docs.python.org/3/library/turtle.html

### Original U.S. States Quiz

https://www.sporcle.com/games/g/states

---

## Future Improvements

Possible extensions:

- Add hints after several incorrect guesses
- Multiple difficulty levels
- Timed mode
- High score tracking
- Display the percentage completed
- Play with countries from other continents
- Interactive zoomable map
- Sound effects

---
