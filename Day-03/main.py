print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("People say a hidden treasure is buried somewhere on this mysterious island")
print("Your mission is to find the treasure without losing your life.")
print("Good luck adventurer!\n")
direction = input("You arrive at a crossroad. Do you go LEFT or RIGHT?\n").lower()
if direction == "left":
    action = input("You reach a lake. Do you SWIM or WAIT for a boat?\n").lower()
    if action == "wait":
        door = input("You safely reach the island and find three magical doors.\n"
                     "Which door do you choose? RED, BLUE or YELLOW?\n").lower()
        if door == "yellow":
            print("Congrats!! You found the treasure!")
            print("You win!")
        elif door == "red":
            print("A giant dragon woke up and wasn't happy to see you")
            print("Game Over!")
        elif door == "blue":
            print("The room froze! You are trapped in ice forever.")
            print("Game Over!")
        else:
            print("You are finding a door that doesn't exist!"
                  " You are trapped in the castle forever")
            print("Game Over!")
    else:
        print("A giant crocodile was waiting in the lake.")
        print("Game over!")
else:
    print("Active Volcano! The ground cracked beneath your feet!")
    print("Game Over!")

