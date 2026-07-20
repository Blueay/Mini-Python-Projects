# 🐍 Snake Game

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Object--Oriented-Programming-success)
![GUI](https://img.shields.io/badge/Turtle-Graphics-green)
![Game](https://img.shields.io/badge/Project-Snake-orange)

A classic **Snake Game** built with Python using the **Turtle Graphics** module and **Object-Oriented Programming (OOP)**.

Control the snake, eat food to grow longer, increase your score, and avoid colliding with the walls or your own tail.

---

## Screenshot

<p align="center">
  <img src="images/gameplay.png" width="700" alt="Snake Game">
</p>

---

## Flowchart

```text
                    Start
                      │
                      ▼
              Create Game Objects
                      │
                      ▼
              Create Snake
                      │
                      ▼
               Create Food
                      │
                      ▼
            Create Scoreboard
                      │
                      ▼
               Start Game Loop
                      │
                      ▼
              Move Snake Forward
                      │
          ┌───────────┼────────────┐
          │           │            │
          ▼           ▼            ▼
     Food Hit?    Wall Hit?    Tail Hit?
          │           │            │
     ┌────┴───┐       │            │
     │        │       │            │
    Yes      No      Yes          Yes
     │        │       │            │
     ▼        │       ▼            ▼
Grow Snake    │   Game Over    Game Over
Increase      │
Score         │
Move Food     │
     │        │
     └────────┴──────────────► Continue
```

---

## Features

- Classic Snake gameplay
- Object-Oriented architecture
- Keyboard controls
- Random food generation
- Snake grows after eating food
- Live score tracking
- Collision detection
- Game Over screen
- Smooth animation using Turtle Graphics

---

## Controls

| Key | Action |
|------|--------|
| ⬆️ Up | Move Up |
| ⬇️ Down | Move Down |
| ⬅️ Left | Move Left |
| ➡️ Right | Move Right |

---

## Project Structure

```text
.
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── README.md
└── images/
    └── gameplay.png
```

---

## Object-Oriented Design

```text
                 main.py
                    │
        ┌───────────┼────────────┐
        │           │            │
        ▼           ▼            ▼
     Snake        Food      Scoreboard
        │           │            │
        └───────────┼────────────┘
                    │
                    ▼
              Game Controller
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/snake-game.git
```

Navigate into the project:

```bash
cd snake-game
```

Run the game:

```bash
python main.py
```

---

## Gameplay

- Guide the snake using the arrow keys.
- Eat the blue food to increase your score.
- Each piece of food makes the snake grow longer.
- Avoid hitting the walls.
- Avoid colliding with your own tail.
- The game ends when a collision occurs.

---

## Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Object composition
- Turtle Graphics
- Keyboard event handling
- Collision detection
- Game loop
- Lists
- Methods
- Screen updates
- Animation
- Random module
- Program state management

---

## Further Reading

### Turtle Graphics

https://docs.python.org/3/library/turtle.html

### Keyboard Events

https://docs.python.org/3/library/turtle.html#turtle.onkey

### Object-Oriented Programming

https://realpython.com/python3-object-oriented-programming/

### Python Classes

https://docs.python.org/3/tutorial/classes.html

### Python Lists

https://developers.google.com/edu/python/lists

---
