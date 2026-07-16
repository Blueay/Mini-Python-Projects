# ☕ Coffee Machine (Object-Oriented Programming)

This project is an object-oriented implementation of the **Coffee Machine** application.

Instead of placing all functionality into a single file, the application is divided into multiple classes with clearly defined responsibilities. The main program coordinates these objects to simulate a real coffee vending machine.

The application allows users to order coffee, processes payments, checks available resources, prepares drinks, and keeps track of the machine's profit.

---

## Flowchart

```text
                     Start
                       │
                       ▼
             Create Machine Objects
                       │
                       ▼
            Ask for Drink Selection
                       │
         ┌─────────────┼──────────────┐
         │             │              │
       report         off         drink order
         │             │              │
         ▼             ▼              ▼
 Display Reports      End      Find Menu Item
                                      │
                                      ▼
                        Resources Sufficient?
                           ┌────────┴────────┐
                           │                 │
                          Yes               No
                           │                 │
                           ▼                 ▼
                     Process Payment    Display Error
                           │
                   Payment Successful?
                      ┌─────┴─────┐
                      │           │
                     Yes         No
                      │           │
                      ▼           ▼
                 Make Coffee   Refund Money
                      │
                      ▼
              Update Resources
                      │
                      ▼
                 Next Customer
```

---

## Features

- Object-Oriented implementation
- Modular project architecture
- Order Espresso, Latte, or Cappuccino
- Resource management
- Automatic payment processing
- Change calculation
- Profit tracking
- Ingredient availability checks
- Coffee preparation simulation
- Machine status reports

---

## Project Structure

```text
.
├── main.py
├── menu.py
├── coffee_maker.py
├── money_machine.py
├── Coffee Machine Classes Documentation.pdf
├── Coffee Machine Program Requirements.pdf
└── README.md
```

---

## Class Responsibilities

### `Menu`

- Stores all available drinks
- Returns available menu options
- Finds a drink by name

### `MenuItem`

- Represents a single coffee drink
- Stores:
  - name
  - ingredients
  - cost

### `CoffeeMaker`

- Tracks machine resources
- Checks ingredient availability
- Makes coffee
- Updates resources
- Prints resource reports

### `MoneyMachine`

- Processes inserted coins
- Calculates change
- Tracks total profit
- Prints profit reports

---

## Object-Oriented Design

```text
                 main.py
                    │
     ┌──────────────┼──────────────┐
     │              │              │
     ▼              ▼              ▼
   Menu       CoffeeMaker    MoneyMachine
     │              │              │
     ▼              ▼              ▼
 MenuItem      Resources      Coin Handling
```

---

## How to Run

```bash
python main.py
```

---

## Example

```text
What would you like to drink?
(espresso/latte/cappuccino):

latte

Please insert coins.

How many quarters?
10

How many dimes?
0

How many nickles?
0

How many pennies?
0

Here is $0.00 in change.

Here is your latte ☕️. Enjoy!
```

---

## Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes
- Objects
- Constructors (`__init__`)
- Methods
- Attributes
- Encapsulation
- Composition
- Modular programming
- Separation of concerns
- Functions
- Dictionaries
- Loops
- Conditional statements
- User input
- Program state management

---

## Further Reading

### Python Classes

https://docs.python.org/3/tutorial/classes.html

### Object-Oriented Programming

https://realpython.com/python3-object-oriented-programming/

### Python Modules

https://docs.python.org/3/tutorial/modules.html

### Python Packages

https://docs.python.org/3/tutorial/modules.html#packages

### Official Python Tutorial

https://docs.python.org/3/tutorial/

---

## Project Evolution

This project is the object-oriented successor to the procedural **Coffee Machine** project.

### Procedural Version

- Functions
- Global variables
- Manual resource management

### Object-Oriented Version

- Classes
- Encapsulation
- Reusable objects
- Modular architecture
- Easier maintenance
- Better scalability

This transition demonstrates how procedural code can be refactored into a clean object-oriented design while preserving the same functionality.
