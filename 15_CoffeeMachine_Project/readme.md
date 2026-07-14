# ☕ Coffee Machine

This project simulates a **coffee machine** in Python.

Users can order different coffee drinks, insert coins for payment, and receive their beverage if sufficient ingredients are available. The machine keeps track of available resources, processes transactions, calculates change, and updates its internal inventory after each successful order.

The project demonstrates how a real-world vending machine can be modeled using Python functions, dictionaries, loops, and program state.

---

## Flowchart

```text
                     Start
                       │
                       ▼
             Ask for Drink Order
                       │
         ┌─────────────┼─────────────┐
         │             │             │
       report         off         coffee
         │             │             │
         ▼             ▼             ▼
 Display Resources    End    Check Resources
                                     │
                           ┌─────────┴─────────┐
                           │                   │
                          Yes                 No
                           │                   │
                           ▼                   ▼
                    Insert Coins      Display Error
                           │                   │
                           ▼                   │
                  Enough Money?                │
                     ┌─────┴─────┐             │
                     │           │             │
                    Yes         No─────────────┘
                     │
                     ▼
             Calculate Change
                     │
                     ▼
             Make Coffee ☕
                     │
                     ▼
            Update Resources
                     │
                     ▼
                Next Customer
```

---

## Features

- Order **Espresso**, **Latte**, or **Cappuccino**
- Check available ingredients and money with the `report` command
- Turn off the machine with the `off` command
- Process coin payments
- Calculate and return change
- Track total profit
- Deduct ingredients after every successful purchase
- Stop serving drinks when ingredients are insufficient

---

## Project Structure

```text
.
├── main.py
├── main_coffeemachine.py
└── README.md
```

---

## How to Run

```bash
python main.py
```

or

```bash
python main_coffeemachine.py
```

---

## Example

```text
What would you like?
(espresso/latte/cappuccino):

latte

Please insert coins.

How many quarters?
10

How many dimes?
0

How many nickels?
0

How many pennies?
0

Here is $0.00 in change.

Here is your latte. ☕ Enjoy!
```

---

## Python methods



| Skill | Used |
|--------|:----:|
| Functions | ✅ |
| Dictionaries | ✅ |
| Nested Dictionaries | ✅ |
| Loops | ✅ |
| Conditionals | ✅ |
| Modular Programming | ✅ |
| User Input | ✅ |
| State Management | ✅ |
| Simulation | ✅ |
| Problem Solving | ✅ |

---

## Further Reading

### Python Dictionaries
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

### Python Functions
https://docs.python.org/3/tutorial/controlflow.html#defining-functions

### Python While Loops
https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming

### Python Global Variables
https://docs.python.org/3/reference/simple_stmts.html#the-global-statement

### Python Data Structures
https://docs.python.org/3/tutorial/datastructures.html
