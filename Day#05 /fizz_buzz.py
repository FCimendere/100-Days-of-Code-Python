"""
PRACTISE : Python Loops
GAME : FizzBuzz
The program should print each number from 1 to 100 in turn.
  When the number is divisible by 3 then instead of printing the number it should print "Fizz".
  When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
  And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
"""

times_3  = "Fizz"
times_5 = "Buzz"

#Create the fizz or buzz or fizz buzz depending on the rules.
#repeat the code as many as a loop.
for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
   print(times_3 + times_5)
  elif i % 3 == 0:
    print (times_3)
  elif i % 5 == 0:
    print(times_5)
  else:
    print(i)