import random
import time


def print_pause(value):
    print(value)
    time.sleep(2)


character = ["fairie", "monster", "witch"]


def won(villain):
    print_pause(f"You won!!,"
                f"You fought bravely and defeated the {villain}\n ")


def lost(villain):
    print_pause("GAME OVER\n"
                f"You were not brave enough,"
                f"The {villain} attacked and defeated you\n")


def exit_game():
    print_pause("Hope to see you soon\n"
                "In case you change your min I'm here :D \n")
    exit(0)


def start(villain):
    storylist = ["You find yourself standing in an open field,\n",
                 "filled with grass and yellow wildflowers.\n",
                 f"Rumor has it that a wicked {villain} is somewhere\n",
                 "around here,and has been terrifying the nearby village,\n",
                 f"The wicked {villain} terrifies the vilage once again,\n"]

    for story in storylist:
        print_pause(story)


def option(villain):
    while True:
        opt = input("What will you do?\n"
                    f"Enter 1 to Fight the {villain}.\n"
                    "Enter 2 to Stay in the house"
                    "and hope it does not attack.\n"
                    "Please enter 1 or 2\n")

        if opt == "1":
            won(villain)
            play_again()
        elif opt == "2":
            lost(villain)
            play_again()
        else:
            print("Invalid response")
            option(villain)


def play_again():
    while True:
        restart = input("Would you like to play again?\n"
                        "Enter y for yes or"
                        " n for no \n")
        if restart == "y":
            print_pause("Very good, You're a hero")
            adv()
        elif restart == "n":
            print_pause("See You Later!")
            exit_game()
        else:
            print("Invalid response")


def adv():
    villain = random.choice(character)
    start(villain)
    option(villain)


adv()
