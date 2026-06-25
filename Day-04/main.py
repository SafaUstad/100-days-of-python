#Let's play rock, paper and scissors with a bot
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Create a list for the options
options = [rock, paper, scissors]

# Take the choice od user as an input
choice = int(input("Choose your choice 0 for rock, 1 for paper, 2 for scissors.\n"))
if choice == 0:
    print("You chose rock")
elif choice == 1:
    print("You chose paper")
elif choice == 2:
    print("You chose scissors")
else:
    print("You chose not a choice")

print(options[choice])

# Let bot choose a choice randomly
random_bot_value = random.randint(0,2)
if random_bot_value == 0:
    print("Bot chose rock")
elif random_bot_value == 1:
    print("Bot chose paper")
else:
    print("Bot chose scissors")

print(options[random_bot_value])

# Create conditions
if choice == random_bot_value:
    print("Tie!")
else:
    if choice == 0 and random_bot_value == 1:
        print("Bot wins!")
    elif choice == 0 and random_bot_value == 2:
        print("You win!")
    elif choice == 1 and random_bot_value == 0:
        print("You win!")
    elif choice == 1 and random_bot_value == 2:
        print("Bot wins!")
    elif choice == 2 and random_bot_value == 0:
        print("Bot wins!")
    elif choice == 2 and random_bot_value == 1:
        print("You win!")

