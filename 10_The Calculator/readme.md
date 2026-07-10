# Calculator

This is a simple **Calculator** application written in Python.

The program performs basic arithmetic operations and allows users to continue calculating with the previous result or start a new calculation at any time.

## Flowchart

```text
                    Start
                      │
                      ▼
                Display Logo
                      │
                      ▼
            Enter First Number
                      │
                      ▼
             Select Operation
                      │
                      ▼
            Enter Second Number
                      │
                      ▼
            Perform Calculation
                      │
                      ▼
              Display Result
                      │
                      ▼
        Continue with Result?
                 ┌────┴────┐
                 │         │
               Yes        No
                 │         │
                 ▼         ▼
      Use Result as     Start New
      First Number     Calculation
                 │         │
                 └────┬────┘
                      │
                      ▼
             Select Operation
```

## Features

- Addition, subtraction, multiplication, and division
- Function-based implementation
- Uses a dictionary to map operators to functions
- Continue calculating with the previous result
- Start a new calculation without restarting the program
- Simple command-line interface

## Project Structure

```text
.
├── art.py
├── The Calculator.py
└── README.md
```

## How to Run

```bash
python "The Calculator.py"
```

## Example

```text
What is the first number?
10

+
-
*
/

Pick an operation:
*

What is the second number?
5

10 * 5 = 50

Type 'y' to continue calculation with 50, or type 'n' to start new calculation:
```

## Concepts Practiced

- Functions
- Dictionaries
- Loops (`while`)
- Recursion
- User input
- Function references
- Arithmetic operations
- Program flow control
