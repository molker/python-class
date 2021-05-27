import sys
from random import randint

'''
    Exercise to create a guessing game
    practice importing packages
    User will run the file with 2 arguments indicating the
    range they want to guess a random number in
'''
try:
    range_start = int(sys.argv[1])
    range_end = int(sys.argv[2])
except ValueError:
    print('Please run again with integers as the run parameters')
    sys.exit()

random_number = randint(range_start, range_end)

while True:
    try:
        guess = int(
            input(f'Guess a number between {range_start} - {range_end}: '))
    except ValueError:
        print('Please enter a valid number')
        continue
    else:
        # Check if guess is in range
        if guess > range_end or guess < range_start:
            print(f'Your guess is outside given range {range_start} - {range_end}. Try again')
        # Check if guess is correct
        elif guess == random_number:
            print('You got it!')
            break
        else:
            print('Nope! Try again')
