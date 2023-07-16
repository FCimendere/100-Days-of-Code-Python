"""
This is a game to find a teasure box inside a dangerous world. 
Depending on the user's way selection, game will continue the next challange or end.
Mainly this game shows the practise of control flows and logical operations.

"""

print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.")

#first way selection.
first_way = input('Where do you want to go? Type "left" or "right"').lower()

#control of the user's way inside the dangerous world. 
if first_way != "left":
  print("Fall into a hole. Game over.")
else:
  second_way = input('What do you want to do? Type "swim" or "wait"').lower()

  if second_way != "wait":
    print("Attacked by trouts. Game over.")
  else:
    third_way = input(
      'Which door do you want to choose? Type "red", "blue" or "yellow"'
    ).lower()
    if third_way == "red":
      print("Burned by fire. Game over.")
    elif third_way == "blue":
      print("Eaten by beasts. Game over.")
    elif third_way == "yellow":
      print("You win!")
    else:
      print("Game Over")
