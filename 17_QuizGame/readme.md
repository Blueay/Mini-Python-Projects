![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Object--Oriented-Programming-success)
![Quiz](https://img.shields.io/badge/Project-Quiz_Game-orange)
![API Data](https://img.shields.io/badge/Data-OpenTDB-informational)

# 🧠 Quiz Game

This project is a command-line **Quiz Game** written in Python using **Object-Oriented Programming (OOP)**.

The application presents a series of **True/False** questions to the player, evaluates each answer, keeps track of the score, and displays the final result after all questions have been answered.

The quiz questions are based on data provided by the **Open Trivia Database (OpenTDB)**.

---

## Flowchart

```text
                     Start
                       │
                       ▼
              Load Question Data
                       │
                       ▼
         Create Question Objects
                       │
                       ▼
           Create QuizBrain Object
                       │
                       ▼
            Questions Remaining?
               ┌────────┴────────┐
               │                 │
              Yes               No
               │                 │
               ▼                 ▼
          Display Question   Show Final Score
               │                 │
               ▼                 ▼
          User Answers         End
               │
               ▼
        Check Correct Answer
               │
               ▼
          Update Score
               │
               └──────────────►
```

---

## Features

- Object-Oriented architecture
- True/False quiz questions
- Automatic score tracking
- Immediate feedback after every answer
- Final score summary
- Question bank created from external data
- Clean separation between data and business logic

---

## Project Structure

```text
.
├── main.py
├── question_model.py
├── quiz_brain.py
├── data_50.py
└── README.md
```

---

## Class Responsibilities

### `Question`

Represents a single quiz question.

Stores:

- Question text
- Correct answer

---

### `QuizBrain`

Controls the quiz logic.

Responsibilities:

- Display questions
- Track current question number
- Validate answers
- Update the player's score
- Determine when the quiz is finished

---

### `main.py`

Coordinates the application by:

- Loading the question data
- Creating `Question` objects
- Initializing the `QuizBrain`
- Running the quiz loop

---

## Object-Oriented Design

```text
                 main.py
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
 Question Objects         QuizBrain
        │                       │
        └───────────┬───────────┘
                    │
                    ▼
              Quiz Game Logic
```

---

## How to Run

```bash
python main.py
```

---

## Example

```text
Q.1: RAM stands for Random Access Memory.
(True/False)?

true

Correct! You got it right.

Your current score is: 1/1


Q.2: The Python programming language gets its name from the British comedy group 'Monty Python'.
(True/False)?

true

Correct! You got it right.
```

---

## Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Attributes
- Methods
- Lists
- Dictionaries
- Loops (`while`, `for`)
- Conditional statements
- User input
- Object composition
- Data modeling
- Program flow control
- Separation of concerns

---

## Further Reading

### Python Classes

https://docs.python.org/3/tutorial/classes.html

### Object-Oriented Programming

https://realpython.com/python3-object-oriented-programming/

### Python Modules

https://docs.python.org/3/tutorial/modules.html

### Python Lists

https://developers.google.com/edu/python/lists

### Open Trivia Database (Question Source)

https://opentdb.com

---

## Data Source

The quiz questions used in this project are provided by the **Open Trivia Database (OpenTDB)**.

OpenTDB is a free API that offers thousands of trivia questions across multiple categories and difficulty levels.

Website:
https://opentdb.com

API Documentation:
https://opentdb.com/api_config.php

---

## Future Improvements

- Load questions directly from the OpenTDB API
- Multiple-choice questions
- Difficulty selection
- Category selection
- Timer for each question
- High score tracking
- Graphical User Interface (GUI)
