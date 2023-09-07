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

money = 0


def report():
    """"Print the balancing resources, no input is needed."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def resources_check(drink):
    """Compare the order drink ingredients with existing ingredients."""
    order_ingredients = MENU[drink]["ingredients"]
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Insufficient {item}")
            return False
    return True


def coin_insert():
    """"Coin processing, no input is needed in the function."""
    print("Insert coins: ")
    total = 0.25 * int(input("How many quarters? "))
    total += 0.10 * int(input("How many dimes? "))
    total += 0.05 * int(input("How many nickles? "))
    total += 0.01 * int(input("How many pennies? "))
    return total


def make_drink(drink):
    """"Calculate the remaining resources after making the drink. Input = drink """
    order_ingredients = MENU[drink]["ingredients"]
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink}. Enjoy! 😁")


on_off = True

while on_off:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "off":
        on_off = False
    elif prompt == "report":
        report()
    else:
        if resources_check(prompt):
            amount_received = coin_insert()
            money += amount_received
            if amount_received < MENU[prompt]["cost"]:
                money -= amount_received
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = amount_received - MENU[prompt]["cost"]
                if change > 0:
                    print(f"Here is ${change:.2f} dollars in change.")
                    money -= change
                make_drink(prompt)
