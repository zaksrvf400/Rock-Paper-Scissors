"""Rock Paper Scissors"""

import random
import sys

# welcome message
print("Welcome to Rock, Paper, Scissors!\n"
"\n"
"To play the game you will choose an attack, Rock, Paper or Scissors, against the computer.\n"
"The computer will also choose an attack against you.\n"
"Whoever wins gets a point.\n"
"Best out of 3 will win.\n"
"\n"
"Would you like to play??\n"
"Press 'Y' to play or 'Q' to quit.")

# Players choice to play or not
while True:
    play = input("> ")
    if play.upper() == "Q":
        sys.exit()
    elif play.upper() == str("Y"):
        print("OK! Let's play!!\n"
              "\n"
              "Press 'R' for Rock, 'P' for Paper and 'S' for Scissors.")
        break
    else:
        print("Please select a valid input...")

# Whole game loop
play = True
while play:
    player_score = 0
    computer_score = 0
    while computer_score < 2 or player_score < 2:

        # Players choice
        while True:
            print("Choose your attack!")
            choices = {"R": "You have chosen rock", "P": "You have chosen paper",
                       "S": "You have chosen scissors"}
            player_choice = input("> ").upper()
            if player_choice == "P":
                print(choices.get("P"))
                break
            elif player_choice == "R":
                print(choices.get("R"))
                break
            elif player_choice == "S":
                print(choices.get("S"))
                break
            else:
                print("Please make a valid selection!")

        # Computer choice
        computer_choice = random.choice(["P", "S", "R"])
        if computer_choice == "S":
            print("The computer has chosen Scissors.\n")
        elif computer_choice == "P":
            print("The computer has chosen Paper.\n")
        elif computer_choice == "R":
            print("The computer has chosen Rock.\n")

        # Result of battle
        if player_choice == computer_choice:
            print("It's a draw!")
        elif player_choice == "P":
            if computer_choice == "S":
                computer_score += 1
                print("Scissors cut paper. Computer wins!\n")
            elif computer_choice == "R":
                player_score += 1
                print("Paper wraps around Rock. Player wins!\n")
        elif player_choice == "S":
            if computer_choice == "P":
                player_score += 1
                print("Scissors cut paper. Player wins!\n")
            elif computer_choice == "R":
                computer_score += 1
                print("Rock smashes scissors. Computer wins!\n")
        elif player_choice == "R":
            if computer_choice == "P":
                computer_score += 1
                print("Paper wraps around rock. Computer wins!\n")
            elif computer_choice == "S":
                player_score += 1
                print("Rock smashes scissors. Player wins!\n")

        # Result of war
        print(f"Scores: Player Score {player_score}: Computer Score {computer_score}!")
        if player_score == 2:
            print(f"You thrashed the computer! Your score of {player_score} beat the computers score of {computer_score}!")
            break
        elif computer_score == 2:
            print(f"The computer thrashed you {computer_score} to {player_score}!")
            break
        else:
            print("On to the next game!\n")

    # Play again option
    print("Would you like to play again?\n")
    play_again = input("> Y or N\n")
    if play_again.upper() == "N":
        print("Thanks for playing!")
        play = False
    else:
        print("Great! Let's start again!")
