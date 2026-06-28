# Coffee Machine Project

# A recipe for all types of coffees
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

# Total resources that are in a machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Update the resources after each serving
def resource_update(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    if coffee != "espresso":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    return resources

# If report wants to be accessed
def report():
    print(f"Water: {resources["water"]}\n"
          f"Milk: {resources['milk']} \n"
          f"Coffee: {resources["coffee"]} \n"
          f"Money: ${money}")

# Check resources sufficient.
def is_enough(resource_left, resource_requirement):
    for item in resource_requirement:
        if resource_left[item] < resource_requirement[item]:
            print(f"Sorry, there isn't enough {item} in the machine.")
            return False
    return True

# Process coins.
def coins(coffee, money):
    if is_enough(resources, MENU[coffee]["ingredients"]):
        penny = int(input("Pennies: "))
        nickel = int(input("Nickels: "))
        dimes = int(input("Dimes: "))
        quarters = int(input("Quarters: "))
        total = penny * 0.01 + nickel * 0.05 + dimes * 0.1 + quarters * 0.25
        # Check transaction successful.
        if total >= MENU[coffee]["cost"]:
            if total > MENU[coffee]["cost"]:
                change = round(total - MENU[coffee]["cost"], 2)
                print(f"Here is ${change} in change.")
            resource_update(coffee)
            money += MENU[coffee]["cost"]
            print(f"Here is your {coffee}. Enjoy!")

        elif total < MENU[coffee]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
    return money


money = 0
to_continue = True

while to_continue:
    to_make = input("\nWhat would you like? (espresso/latte/cappuccino):").lower()
    if to_make == "espresso":
        money = coins("espresso", money)

    elif to_make == "latte":
        money = coins("latte", money)

    elif to_make == "cappuccino":
        money = coins("cappuccino", money)

    # Print report.
    elif to_make == "report":
        report()

    # Turn off the Coffee Machine by entering “off” to the prompt.
    elif to_make == "off":
        to_continue = False

