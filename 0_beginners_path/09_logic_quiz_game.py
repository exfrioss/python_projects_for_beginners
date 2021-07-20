"""
The quiz game asks the player questions about animals. 
They have tthree chances to answer each question you don't want to take the quiz too difficult.
Each correct answer will score a point.
At the end of the game, the program will reveal the player's final score.

The quiz game uses a function; a block code with a name that performs a specific task.
A function allows you to use the same code several times, without haven to type everything each time.
Python has a lot of built-in functions, but it also allows you to create your funcitons.

The program should continue to check if there are any questions to ask and if the player has exahusted all 
his chances. The score is stored in a variable during the game. Once chance all questions have been answered,
the game ends.
"""

def check_gues(guess, answer):
    global score
    still_guessing = True
    attemp = 0
    while still_guessing and attemp < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score += 1
            still_guessing = False
        else:
            if attemp < 2:
                guess = input("Sorry Wrong Answer, try again: ")
            attemp += 1
    if attemp == 3:
        print("The correct answer is ", answer)

score = 0
print('Guess the animal')
guess1 = input("Wich bear lives at the North Pole?: ")
check_gues(guess1, 'polar bear')
guess2 = input("Wich is the fastest land animal?: ")
check_gues(guess2, 'cheetah')
guess3 = input("Wich is the larget animal?: ")
check_gues(guess3, 'blue whale')
print("Your score is: "+str(score))