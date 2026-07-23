# 🐍 Snake Game (High Score Edition)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Object--Oriented-Programming-success)
![Turtle](https://img.shields.io/badge/GUI-Turtle_Graphics-green)
![Game](https://img.shields.io/badge/Project-Snake-orange)

A classic **Snake Game** built with Python using **Object-Oriented Programming (OOP)** and the **Turtle Graphics** module.

This version introduces a **persistent high score system**. Instead of resetting after each game, the highest score is stored in a local text file and automatically loaded the next time the game starts.

---

## Screenshot

<p align="center">
  <img src="images/snake_game_highscore.png" width="700" alt="Snake Game">
</p>

---

## Features

- 🐍 Classic Snake gameplay
- 🍎 Random food generation
- 📈 Live score tracking
- 🏆 Persistent high score
- 💾 High score saved to `data.txt`
- 🎮 Smooth keyboard controls
- 💥 Collision detection
- 🔄 Automatic game reset after collision
- 🧩 Object-Oriented project structure

---

## Controls

| Key | Action |
|------|--------|
| ⬆️ Up | Move Up |
| ⬇️ Down | Move Down |
| ⬅️ Left | Move Left |
| ➡️ Right | Move Right |

---

## Flowchart

```text
                    Start
                      │
                      ▼
              Load High Score
                      │
                      ▼
              Create Game Objects
                      │
                      ▼
               Start Game Loop
                      │
                      ▼
              Move Snake Forward
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   Food Hit?     Wall Hit?     Tail Hit?
        │             │             │
      Yes           Yes           Yes
        │             │             │
        ▼             ▼             ▼
 Increase Score   Save High Score  Save High Score
 Extend Snake     Reset Game       Reset Game
 Move Food
        │
        ▼
    Continue Game
```

---

## Project Structure

```text
Snake-Game/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── data.txt
├── README.md
└── images/
    └── snake_game_highscore.png
```

---

## High Score System

The highest score is stored in a local text file:

```text
data.txt
```

When the game starts:

- the previous high score is loaded
- the current score begins at **0**

When the player beats the existing record:

- the high score is updated
- the new value is written back to `data.txt`

This allows the best score to persist even after closing the game.

---

## How to Run

```bash
python main.py
```

---

## Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes and Objects
- Turtle Graphics
- File Handling (`open()`)
- Reading and writing text files
- Persistent data storage
- Collision detection
- Keyboard event handling
- Lists
- Game loops
- Animation
- Program state management

---

## Further Reading

### Python Turtle Graphics

https://docs.python.org/3/library/turtle.html

### Python File Handling

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

### Python `open()`

https://docs.python.org/3/library/functions.html#open

### Python Classes

https://docs.python.org/3/tutorial/classes.html

---

## Future Improvements

Possible enhancements:

- Save multiple high scores
- Player names
- Pause functionality
- Difficulty levels
- Sound effects
- Obstacles
- Different snake skins
- Start menu
- Restart button
