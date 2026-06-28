# Coffee Machine with OOP
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create Objects 
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    # Input the choice of user
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    
    # Report the amount of resources if keyword 'report' is inputted
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
        
    # Switch off the machine if keyword 'off' is inputted
    elif choice == "off":
        is_on = False
        
    # Check if resources are enough and enough payment is made -> Make the coffee
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



