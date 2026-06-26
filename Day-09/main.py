#Blind Auction Project
from art import logo
print(logo)

# Compare bids in dictionary
def compare():
    highest_bid = 0
    for key in bids:
        if(bids[key] > highest_bid):
            highest_bid = bids[key]
            winner = key
    print(f"The winner is {winner} with the highest bid of ${highest_bid}")

to_continue = True
bids = {}
while to_continue:
    # Ask the user for input
    name = input("What is your name? ")
    bid_value = int(input("What is your bid? $"))

    # Save data into dictionary {name: price}
    bids[name] = bid_value

    # Whether if new bids need to be added
    more_bidders = input("Are there any other bidders? Yes or No\n").lower()
    print("\n" * 50)
    if more_bidders == "no":
        to_continue = False
        compare()

