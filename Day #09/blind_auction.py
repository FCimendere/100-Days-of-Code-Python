import os
import time

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print("Welcome to the secret auction program.")


def highest_bid(bid_info):
    highest = 0
    winner = ""
    for bidder in bid_info:
        bid_amount = bid_info[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")


bid_info = {}

decision = True

while decision:
    name = input("What is your name? ")
    offer = int(input("What is your bid? $"))

    bid_info[name] = offer

    my_choice = input("Are there any other bidders? Type 'yes' or 'no'")

    if my_choice == "no":
        decision = False
        time.sleep(1)
        os.system('clear')
        highest_bid(bid_info)
    elif my_choice == "yes":
        time.sleep(1)
        os.system('clear')
