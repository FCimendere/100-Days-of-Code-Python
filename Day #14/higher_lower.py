from art_higher_lower import logo
import random
import os
from time import sleep

score = 0

TITLE = {
  1: {
    'name': 'Cristiano Ronaldo',
    'info': 'Footballer from Portugal',
    'ratio': 596
  },
  2: {
    'name': 'Lionel Messi',
    'info': 'Footballer from Argentina',
    'ratio': 478
  },
  3: {
    'name': 'Selena Gomez',
    'info': 'Musician / Actress / Businesswoman	from USA',
    'ratio': 476
  },
  4: {
    'name': 'Kylie Jenner',
    'info': 'TV Personality / Model / Businesswoman	from USA',
    'ratio': 397
  },
  5: {
    'name': 'Dwayne Johnson',
    'info': 'Actor/ Professional Wrestler from USA',
    'ratio': 387
  },
  6: {
    'name': 'Ariana Grande',
    'info': 'Musician/Actress from USA',
    'ratio': 377
  },
  7: {
    'name': 'Kim Kardashian',
    'info': 'TV Personality / Model / Businesswoman from USA',
    'ratio': 362
  },
  8: {
    'name': 'Beyonce',
    'info': 'Musician from USA',
    'ratio': 314
  },
  9: {
    'name': 'National Geographic',
    'info': 'Magazine from USA',
    'ratio': 281
  },
  10: {
    'name': 'NASA',
    'info': 'Space Agency from USA',
    'ratio': 94
  },
}

def get_title_item():
    '''
    This function create a random number to find a item in TITLE dict.
    Returns a random item.
    '''
    num_rand = random.randint(1, 10)
    my_title_item = []
    get_name = TITLE[num_rand]['name']
    get_info = TITLE[num_rand]['info']
    get_ratio = TITLE[num_rand]['ratio']

    my_title_item.append(get_name)
    my_title_item.append(get_info)
    my_title_item.append(get_ratio)
    return my_title_item

def collect_items():
    '''
    This function creates the two items from the title dict.
    Put those items in the list for the comparing in future steps.
    Returns a list with two items from title.
    '''
    selected_two_items = []
    #two different person creation.
    first_item = get_title_item()
    second_item = get_title_item()
    if first_item[0] == second_item[0]:
        second_item = get_title_item()
    print(f"{first_item[0]} has {first_item[2]} avarage followers.")
    # print(f"LOG---{second_item}")
    selected_two_items.append(first_item)
    selected_two_items.append(second_item)
    return selected_two_items

def next_round(two_items):
    '''
    This function provide continuing of the game. 
    Second item replaces first item and the function create a second random item.
    Returns  new two items list.
    '''
    two_items[0] = two_items[1]
    two_items[1] = get_title_item()
    if two_items[1] == two_items[0]:
        two_items[1] = get_title_item()
    # print(f"LOG - {two_items}")
    print("")
    print(f"{two_items[0][0]} has {two_items[0][2]} avarage followers.")
    user_selection(two_items)
    return two_items


def user_selection(two_items):
    '''
    This function control user's decision. 
    User decide that the second item is higher or lower. 
    Print the user score on screen.
    Call the next_round for contunie.
    '''

    my_select = input(
        f"Please type {two_items[1][0]} has higher: 'h' or lower :'l':  ")
    
    if (my_select == 'h'and two_items[1][2] >= two_items[0][2]) or (my_select == 'l'and two_items[1][2] <= two_items[0][2]):
        global score
        score += 1 
        print(f"Your score is: {score}")
        next_round(two_items)
    else:
        print("That‘s a terrible score. The average score is 3.2. Put some effort into it :)")
        # set_high_score(high_score, score)
        print(f"Your total score is: {score}")
        play_again()
    
def play_again():
    sleep(2)
    os.system('clear')
    
    decision = input("Do you want to play again? Type 'y' for yes, 'n' for no: ")
    if decision == 'y':
        game()
    elif decision == 'n': 
        print("Thanks for playing!")

def game():
    '''
    This functions for playin the all game from beginning. 
    prints logo, call items, and control user selection.
    '''
    print(logo)
    global score
    score = 0
    two_items = collect_items()
    user_selection(two_items)
 
game()