# 🐢 Turtle Crossing Game

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Object--Oriented-Programming-success)
![Turtle](https://img.shields.io/badge/GUI-Turtle_Graphics-green)
![Game](https://img.shields.io/badge/Project-Turtle_Crossing-orange)

A simple arcade-style **Turtle Crossing Game** built with Python using the **Turtle Graphics** module.

Your goal is to safely guide the turtle across a busy road while avoiding incoming cars. Every successful crossing advances you to the next level, where the traffic becomes faster and the challenge increases.

---

## Screenshots

### Gameplay

<p align="center">
  <img src="images/turtle_crossing_level1.png" width="700" alt="Gameplay Screenshot">
</p>

### Game Over

<p align="center">
  <img src="images/turtle_crossing_game_over.png" width="700" alt="Game Over Screenshot">
</p>

---

## Features

- Object-Oriented design
- Randomly generated traffic
- Increasing difficulty
- Level progression
- Collision detection
- Keyboard controls
- Automatic speed increase
- Game Over screen
- Smooth Turtle Graphics animation

---

## Controls

| Key | Action |
|------|--------|
| ⬆️ Up Arrow | Move the turtle forward |

---

## Flowchart

```text
                     Start
                       │
                       ▼
               Create Game Objects
                       │
                       ▼
        Create Player, Cars & Scoreboard
                       │
                       ▼
               Start Game Loop
                       │
                       ▼
             Generate Random Cars
                       │
                       ▼
                Move All Cars
                       │
          ┌────────────┼─────────────┐
          │            │             │
          ▼            ▼             ▼
    Collision?   Finish Line?   Continue
          │            │
        Yes           Yes
          │            │
          ▼            ▼
    Game Over     Increase Level
                       │
               Increase Car Speed
                       │
               Reset Player
                       │
                       ▼
                  Continue Game
```

---

## Project Structure

```text
Turtle-Crossing-Game/
│
├── main.py
├── player.py
├── car_manager.py
├── scoreboard.py
├── README.md
└── images/
    ├── turtle_crossing_level1.png
    └── turtle_crossing_game_over.png
```

---

## Class Responsibilities

### `Player`

Responsible for:

- Creating the turtle player
- Moving upward
- Resetting the player's position
- Detecting when the finish line has been reached

---

### `CarManager`

Responsible for:

- Creating new cars
- Moving all cars
- Increasing traffic speed after every level
- Managing all car objects

---

### `Scoreboard`

Responsible for:

- Displaying the current level
- Updating the level
- Displaying the Game Over message

---

### `main.py`

Coordinates the entire game:

- Screen setup
- Object creation
- Keyboard controls
- Game loop
- Collision detection
- Level progression
- Difficulty scaling

---

## Object-Oriented Design

```text
                    main.py
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
     Player      CarManager     Scoreboard
                        │
                        ▼
                   Car Objects
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/turtle-crossing-game.git
```

Navigate to the project folder:

```bash
cd turtle-crossing-game
```

Run the game:

```bash
python main.py
```

---

## Gameplay

1. Press the **Up Arrow** to move the turtle.
2. Cross the road without hitting a car.
3. Reach the finish line to advance to the next level.
4. Every new level increases the speed of the traffic.
5. The game ends when the turtle collides with a car.

---

## Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Object composition
- Turtle Graphics
- Random module
- Lists
- Loops
- Collision detection
- Animation
- Keyboard events
- Level progression
- Dynamic object creation
- Game loops
- Program state management

---

## Further Reading

### Python Turtle Graphics

https://docs.python.org/3/library/turtle.html

### Python Classes

https://docs.python.org/3/tutorial/classes.html

### Object-Oriented Programming

https://realpython.com/python3-object-oriented-programming/

### Python Random Module

https://docs.python.org/3/library/random.html

---

## Future Improvements

Ideas for extending the game:

- Add left and right movement
- Add multiple lanes with different speeds
- Introduce obstacles
- Save the highest level
- Add lives instead of instant game over
- Pause and restart functionality
- Background music and sound effects
- Animated finish line
- Difficulty selection
- Different turtle skins

---

## Author

Created as part of my Python learning journey to practice Object-Oriented Programming, game development, animation, event handling, and Turtle Graphics.
