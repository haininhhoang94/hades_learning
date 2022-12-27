"""
Guess my number app

Conditional
if TEST:
   conditional code
   conditional code
elif TEST:
   conditional code
else:
    conditional code

Loops
while TEST:
    loop code
    loop code
    loop code

importing modules
import os
print(os.sys.version)

random numbers:
    random.randint(low, high)
"""

import os
import random

print(os.sys.version)

print("--------------------------------------")
print("GUESS THE NUMBER APP")
print("--------------------------------------")

status = False
result = random.randint(0, 100)

while status == False:
    number = input("Guess a number between 0 and 100: ")
    number = int(number)
    if number > result:
        print("Sorry but {} is HIGHER than the number".format(number))
    elif number < result:
        print("Sorry but {} is LOWER than the number".format(number))
    else:
        print("YES! You've got it. The number was {}".format(result))
        print("The game end here!")
        status = True
