# The Blackjack Capstone Project
from art import logo
import random

# Choose random value from cards
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Take a list of cards and return the score calculated from the cards
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Compare who won
def compare(user, bot):
    if user == bot:
        return "Tie!"
    elif bot == 0:
        return "BlackJack! Bot wins!"
    elif user == 0:
        return "BlackJack! You win!"
    elif user == 21:
        return "You win!"
    elif bot > 21:
        return "You win!"
    elif bot == 21:
        return "Bot wins!"
    elif user > bot:
        return "You win!"
    elif bot > user:
        return "Bot wins!"

# To continue playing or not
def want_to_play():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == 'y':
        return True
    else:
        return False

def blackjack():
    print(logo)

    # Create user and bots cards list
    user_cards = []
    bot_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        bot_cards.append(deal_card())

    # Calculate the sum of the cards
    user_score = calculate_score(user_cards)
    bot_score = calculate_score(bot_cards)

    print(f"Your cards: {user_cards}, Current score: {user_score}")
    print(f"Bot's first card : {bot_cards[0]}")

    # Directly return to the end of the code
    if user_score == 0 or bot_score == 0:
        return compare(user_score, bot_score)

    is_game_over = True
    while is_game_over and user_score < 21:
        # Take input to continue hitting or pass to the bot
        choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if choice == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, Current score: {user_score}")
            if user_score > 21:
                return "Bot wins!"
        elif choice == 'n':
            is_game_over = False

    # Bot needs to draw cards until the sum is 17 or more
    while bot_score < 17:
            bot_cards.append(deal_card())
            bot_score = calculate_score(bot_cards)

    print(f"Bot's final hand: {bot_cards}, Final score: {bot_score}")
    return compare(user_score, bot_score)

while want_to_play():
    print("\n" * 25)
    print(blackjack())
