"""
PRACTISE:Functions with outputs
GAME: BlackJack 
Blackjack hands are scored by their point total. 
The hand with the highest total wins as long as it doesn't exceed 21; a hand with a higher total than 21 is said to bust. 
Cards 2 through 10 are worth their face value, and face cards (jack, queen, king) are also worth 10. 
An ace's value is 11 unless this would cause the player to bust, in which case it is worth 1. 
A hand in which an ace's value is counted as 11 is called a soft hand, because it cannot be busted if the player draws another card.
"""

import random
import os
import time

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """
    This function returns a random card from the deck.
    """
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    This function returns sum of the cards.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def comparison(user_score, computer_score):
  """
  This function returns winner's situation depending on comparison between hands.
  """
  if user_score > 21 and computer_score > 21: 
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
    """
    This function calls the main game.
    """
  print(logo)
  user_cards = []
  computer_cards = []
  
  is_game_over =  False

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_sum = calculate_score(user_cards)
    pc_sum = calculate_score(computer_cards)
    print(f" your cards {user_cards}, current score: {user_sum},")
    print(f" computer first card {computer_cards[0]}")
    
    if user_sum == 0 or user_sum > 21 or pc_sum == 0:
      is_game_over = True
    
    else:
      decision = input("\nType 'y' to get another card, type 'n' to pass: ")
      if decision == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True


  while pc_sum!= 0 and pc_sum < 17:
    computer_cards.append(deal_card())
    pc_sum = calculate_score(computer_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_sum}")
  print(f"Computer's final hand: {computer_cards}, final score: {pc_sum}\n")
  print (comparison(user_sum, pc_sum))

#Depending on the user's decision the game will be played again.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    time.sleep(1)
    os.system('clear')
    play_game()