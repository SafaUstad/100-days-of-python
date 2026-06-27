# Number Guessing Game
import random
from art import logo

print(logo)

# Compare the number that is to be guessed and the user guess
def compare( num1, num2 ):
    if num1 > num2:
        return "Too Low"
    elif num1 < num2:
        return "Too High"
    else:
        return 1 and "Yoohoo! You Got it!"

# The value or val depends on difficulty level
def chance(val):
    guessed = False
    lives = val

    # Until the lives go zero - repeat input of guesses
    for i in range(val):
        if guessed == False:
            print(f"\n*****You have {lives} lives*****")
            guess = int(input("Make a Guess: "))
            if to_guess == guess:
                guessed = True
                print(compare(to_guess, guess))
            else:
                print(compare(to_guess, guess))
                lives -= 1
                if lives == 0:
                    print("\n*****Ran out of guesses! Refresh the page and Try again*****")
                    return
                print("Guess Again")

print("Welcome to the Number Guess Game!!")
print("I am thinking of a number between 1 and 100.")
level = input("Choose level of difficulty: Easy or Hard: ").lower()

# Make a random value to be guessed
to_guess = random.randint(1,100)

if level == "easy":
   chance(10)

elif level == "hard":
   chance(5)

else:
    print("No Such Choice")
