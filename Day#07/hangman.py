#Hangman Game
"""
PRACTISE:List -Loops - Randomisation - Control Flow
GAME : Hangman
In this game, one player selects a word. Other players have a certain number of guesses to guess the characters in the word. If the players are able to guess the characters in the entire word within certain attempts, they win
"""

import random

word_list = [
    'absurd',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bikini',
    'blitz',
    'buckaroo',
    'buffalo',
    'buzzwords',
    'caliph',
    'cobweb',
    'crypt',
    'duplex',
    'dwarves',
    'embezzle',
    'exodus',
    'fixable',
    'funny',
    'galaxy',
    'galvanize',
    'haiku',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jazzy',
    'jockey',
    'jukebox',
    'jumbo',
    'kayak',
    'kiosk',
    'klutz',
    'lengths',
    'lucky',
    'luxury',
    'microwave',
    'nightclub',
    'nowadays',
    'onyx',
    'oxygen',
    'pajama',
    'peekaboo',
    'pixel',
    'puppy',
    'quartz',
    'queue',
    'quiz',
    'rhythm',
    'scratch',
    'staff',
    'strength',
    'subway',
    'swivel',
    'syndrome',
    'topaz',
    'transcript',
    'twelfth',
    'unknown',
    'unzip',
    'uptown',
    'vodka',
    'voodoo',
    'walkway',
    'wheezy',
    'whiskey',
    'wimpy',
    'witchcraft',
    'wizard',
    'xylophone',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zodiac',
    'zombie',
]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
print("Welcome to the hangman game.")

for _ in range(word_length):
    display += "_"
print(f"Your puzzle word is: {' '.join(display)}")


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])