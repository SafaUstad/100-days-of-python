#Calculator
from art import logo
print(logo)

# Write functions for various operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Create a dictionary for all operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    # Input first number
    num1 = float(input("What's the first number? "))

    to_continue = True

    while to_continue:
        # Print all operations to selct from
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an operation: ")

        # Input next number
        num2 = float(input("What's the next number? "))

        # Perform operation
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # User wants to continue with the operation or restart
        choice = input(f"Type 'y' to continue with {answer} or type 'n' to restart: ")
        if choice == "y":
            num1 = answer
        else:
            to_continue = False
            print("\n" * 25)
            # Recursion - Function calling itself
            calculator()

# Call function
calculator()
