import random

#dice rolling simulator

def roll_dice():
    dice_number = random.randint(1,6)
    print("Enter 'done' to end the program")
    user_input = input("Type 'roll' to roll the dice: ").lower()
    print(f"You rolled {dice_number}")
    if user_input == "done":
        quit()
    print("The program terminated successfully")


roll_dice()



