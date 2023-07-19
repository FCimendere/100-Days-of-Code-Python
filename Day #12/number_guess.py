#Game : Number Guess
"""
PRACTISE: Scope & Functions with outputs
GAME: Number Guessing
Program will create a random number between 1-100. User need to find this number by guessing. 
There is two leel difficulties: easy or hard.
If user select easy, user need to find correct answer in 10 times. 
If user select hard, user need to find coreect answer in 5 times. 
"""

import random
from art_number_guess import logo
import os
import time


def set_difficulty():
    #defining the difficulty level. hard gives 5 trials, easy gives 10 trials.
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "hard":
        return 5
    elif difficulty == "easy":
        return 10


def set_random_num():
    #random number selection by computer
    pc_selection = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    #print(f"psst! your number is {pc_selection}")
    return pc_selection


def play_game():
    """
    This part will execute the all game.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")

    pc_selection = set_random_num()
    attemption_level = set_difficulty()

    condition = True
    while condition:
        print(
            f"You have {attemption_level} attempts remaining to guess the number."
        )

        my_guess = int(input("Make a guess: "))

        if my_guess == pc_selection:
            print(f"You guessed the correct number as {my_guess}. You WIN!")
            condition = False
        elif my_guess > pc_selection:
            print("Too High.")
            if not attemption_level > 0:
                print("Guess again\n")
        elif my_guess < pc_selection:
            print("Too Low.")
            if not attemption_level > 0:
                print("Guess again\n")

        attemption_level -= 1

        if attemption_level == 0 and my_guess != pc_selection:
            print("You've run out of guesses, you lose.")
            condition = False


play_game()
play_again = input(
    "\nDo you want to play again? Type for yes: 'y' or for no: 'n': ")
if play_again == "y":
    time.sleep(1)
    os.system('clear')
    play_game()
else:
    print("Thank you for playing")
