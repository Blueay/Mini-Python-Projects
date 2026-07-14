from http.cookiejar import request_port

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0.00

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

# 1. print report
# 2. Check resources sufficient
# 3. Process coins
# 4. Check transaction successful
# 5. Make coffee

# TODO: 1. Print report of all coffee machine resources
# TODO: 2. Check resources sufficient to make drink order

# Prompt user by asking "what would you like?"

def report_format(resource, money):
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    return (
        f"\nWater:    {water}ml \n"    
        f"Milk:     {milk}ml \n"
        f"Coffee:   {coffee}g \n"
        f"Money:    {money:.2f}$\n"
    )


def process_coins():
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (
        quarters * 0.25
        + dimes * 0.10
        + nickels * 0.05
        + pennies * 0.01
    )

    return round(total, 2)

def money_change(money_received, drink_cost):

    if money_received < drink_cost:
        print("Sorry, there is not enough money. Money refunded.")
        return False

    elif money_received > drink_cost:
        change = money_received - drink_cost
        print(f"Here is ${change:.2f} in change.")

        global profit
        profit += drink_cost

        return True

    else:
        print("Payment received. No change.")
        return True



def coffee_request():


    user_request = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    if user_request == "off":
        return False

    elif user_request == "report":
        print(f"Remaining resources:\n {report_format(resources, profit)}")
        return True

    elif user_request not in MENU:
        print("Invalid order. Please choose espresso, latte or cappuccino.")
        return True

    drink = MENU[user_request]
    ingredients = drink["ingredients"]
    drink_cost = drink["cost"]


    #   Check ingredients before asking for money
    for ingredient, required_amount in ingredients.items():
        if resources[ingredient] < required_amount:
            print(f"Sorry, there is not enough {ingredient}.")
            print("The coffee machine is now out of service.")
            return False

    money_inserted = process_coins()

    payment_successful = money_change(money_inserted, drink_cost)

    if not payment_successful:
        return True

    # Add the drink price to the machine's money


    # print(f"You inserted ${money_inserted:.2f}.")
    # print(f"The {user_request} costs ${drink_cost:.2f}.")


    # Deduct ingredients
    for ingredient, required_amount in ingredients.items():
        resources[ingredient] -= required_amount

    print(f"Here is your {user_request}. ☕️ Enjoy!")
    #print(f"Remaining resources: {resources}")

    return True


coffee_machine_in_service = True

while coffee_machine_in_service:
    coffee_machine_in_service = coffee_request()
