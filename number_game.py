import random

# Get a random number
hidden_number = random.randrange(1, 100)
print(hidden_number)
while True:
    # Ask user to guess the number
    guess_number = input("Guess a number from 1 to 100: ")
    # Use isnumeric (returns True if all numbers, False if letters)
    if guess_number.isnumeric() == False:
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
