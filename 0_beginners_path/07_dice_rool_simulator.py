"""
Dice Roll Simulator with Python
The dice Dice Roll Simulator can be done by choosing a random integer btween 1 and 6 for
which we can use the random module in the python programing language.

To simulate a dice roll with python, we'll be using the random module in the python.
The random module can be imported easily into your code as it is preinstalled in the python
programing language.
"""
# importing module for random number generation
import random

# range of the values of a dice
min_val = 1
max_val = 6

# To loop the rolling through user input
roll_again = "yes"

# loop
while roll_again == 'yes' or roll_again == 'y':
    print("Rolling The Dices...")
    print("The values are: ")
    
    # Generating and printing 1st random integer from 1 to 6
    print(random.randint(min_val, max_val))
    
    # Generating and printing 2nd random integer from 1 to 6
    print(random.randint(min_val, max_val))
    
    # asking user to roll the dice angain. Any input other than yes or y will terminate de loop.
    roll_again = input("Roll the Dices Angain? ")