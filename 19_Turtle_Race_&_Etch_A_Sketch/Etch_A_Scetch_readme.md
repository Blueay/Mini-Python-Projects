# 🎨 Etch-a-Sketch App

This project recreates the classic **Etch-a-Sketch** drawing toy using Python's **Turtle Graphics** module.

The user controls the turtle with the keyboard to draw freely on the screen. The drawing can be cleared at any time, returning the turtle to its starting position.

---

## Screenshot

<p align="center">
  <img src="etch_a_sketch_demo.png" width="700" alt="Etch-a-Sketch App">
</p>

---

## Flowchart

```text
                 Start
                   │
                   ▼
            Create Turtle
                   │
                   ▼
          Listen for Keyboard
                   │
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
    W → Forward  A → Left  D → Right
        │                     │
        ▼                     ▼
   S → Backward        Q → Clear Screen
        │
        ▼
   Continue Drawing
```

---

## Controls

| Key | Action |
|------|--------|
| **W** | Move Forward |
| **S** | Move Backward |
| **A** | Turn Left |
| **D** | Turn Right |
| **Q** | Clear Drawing & Return Home |

---

## Features

- Keyboard-controlled turtle
- Draw freely on the canvas
- Clear the screen instantly
- Reset turtle to the starting position
- Beginner-friendly Turtle Graphics project

---

## Project Structure

```text
.
├── Etch_a_Sketch_App.py
├── etch_a_sketch_demo.png
└── README.md
```

---

## How to Run

```bash
python Etch_a_Sketch_App.py
```

---

## Concepts Practiced

- Turtle Graphics
- Event listeners
- Keyboard input
- Functions
- Screen events
- Object-Oriented Programming
- Methods
- Program interaction

---

## Further Reading

### Turtle Graphics

https://docs.python.org/3/library/turtle.html

### Keyboard Events

https://docs.python.org/3/library/turtle.html#turtle.onkey

### Event-driven Programming

https://docs.python.org/3/library/tkinter.html
