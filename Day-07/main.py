#Hangman Game
import random
import hangman_art
import hangman_words

# Represent logo
print(hangman_art.logo)

# Take a random choice from the word_list
chosen_word = random.choice(hangman_words.word_list)

# User must know how many letters does the word consist
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(f"Word : {placeholder}")

game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"*********You have {lives} lives*********")
    guess = input("Guess a letter: ").lower()

    display = ""

    # If the user selects the same guess
    if guess in correct_letters:
        print("You have already guessed this letter")

    # Update the display
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Word: {display}")

    # User has guessed the word
    if display == chosen_word:
        game_over = True
        print("**********Yoohoo! You guessed the word!******")

    # User had a wrong guess
    if guess not in chosen_word:
        lives -= 1
        print("******You Lose a Life*******")
        if lives == 0:
            game_over = True
            print(f"*******The word was {chosen_word}. You Lose!!*****")

    # Display the hangman with respect to the lives
    print(hangman_art.stages[lives])
