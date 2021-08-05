# Exercise Testing
from random import randint
import sys


def getInput(guess, answer) -> bool:
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                return True
        else:
            print('hey bozo, I said 1~10')
            return False
    except ValueError as err:
        return err
    except TypeError as err:
        return err


if __name__ == '__main__':
    # generate a number 1~10
    answer = randint(1, 10)

    # input from user?
    # check that input is a number 1~10
    while True:
        guess = int(input('guess a number 1~10:  '))
        if getInput(guess, answer):
            break
