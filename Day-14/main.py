# Higher Lower Game Project
import random
import  art
from game_data import data

# Random func
def random_choice(option1=None):
    choice = random.choice(data)
    # Make sure both options are not same
    if option1 is not None and choice["follower_count"] == option1["follower_count"]:
        return random_choice(option1)
    return choice

# Compare two celebrities follower counts
def compare(value1, value2):
    guess = input("Who might have more followers? 'A' or 'B': ").lower()
    if value1 > value2:
        if guess == "a":
            return 1
        elif guess == "b":
            return 0
    elif value2 > value1:
        if guess == "a":
            return 0
        elif guess == "b":
            return 1

# Display Option 1 vs Option 2
def display(option1, option2):
    print(f"Compare A: {option1["name"]}, a {option1["description"]}, "
          f"from {option1["country"]}.")
    print(art.vs)
    print(f"Against B: {option2["name"]}, a {option2["description"]}, "
          f"from {option2["country"]}.")


print(art.logo)
option1 = random_choice()
option2 = random_choice(option1)
display(option1, option2)

# Continue until a wrong choice is chosen
is_game_over = False
# Increase the score with every correct choice
score = 0
while not is_game_over:

    result = compare(option1["follower_count"], option2["follower_count"])

    if result == 1:
        score += 1
        print("\n" * 25)
        print(art.logo)
        print(f"You're right! Current score: {score}")
        # Store the value of Option B in Option A
        option1 = option2
        option2 = random_choice(option1)
        display(option1, option2)

    elif result == 0:
        print("\n"*25)
        print(art.logo)
        print(f"Oh No! The End! Final score: {score}")
        is_game_over = True




