'''Create new repo called homework2
Create  new branch called homework_game
Write a game “guess a number”
Logic of the game.
Your create and save random number for each game (from 1 to 100)
Then you ask user to guess this number
After user guess
If user guess the number write “Congratulations! And stop the game.
If user did not guess tell if his guess was higher or below the expected, then ask him to guess one more time.
You will need - https://docs.python.org/3/library/random.html module to create random number
Create new pull-request to your main/master branch and send link to it as answer'''

import random

# Get a random number
hidden_number = random.randrange(1, 100, 1)
print(hidden_number)
while True:
    # Ask user to guess the number
    guess_number = input("Guess a number from 1 to 100: ")
    # Check based on the ASCII table  if it is letter based on it is index
    if guess_number >= "A":
        print("Please enter a valid number")
    # now that we know it is not a letter, then we start the game
    else:
        guess_number = int(guess_number)  # make the input str an int so we can then compare the input with int
        if guess_number > 100:
            print("Make sure it is between 1-100!")
            continue
        if guess_number < 1:
            print("Make sure it is between 1-100!")
            continue
        # Tell user his guess is  lower then hidden number
        elif guess_number < hidden_number:
            print("Your guess is lower than expected.")
        # Tell user his guess is  higher then hidden number
        elif guess_number > hidden_number:
            print("Your guess is higher than expected.")
        # If user guess the right number write “Congratulations! And stop the game
        elif guess_number == hidden_number:
            print("Congratulations!!!")
            break
