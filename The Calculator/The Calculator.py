import art

#1 Define the 4 operations

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#2 Store them in a dictionary as values

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#3 Use the dictionary operations to perform the calculations.
# Multiplication example 4 * 8

#print(operations["*"](4,8))

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?:  "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation:  ")
        num2 = float(input("What is the second number?:  "))

        #if operator in operations:
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start new calculation:  ")

        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()