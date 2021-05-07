import random
import sys

def computer_guess_the_number(min, max):
    print(f'\nPlease think of a number between {min} and {max} inclusive!')
    input('Press any key when ready ...')

    while(1):
        guess = (min + max) // 2                # integer division
        resp = input('Is your number [' + str(guess) + '].  Guess is [hi  lo  correct]?\t')
        if (resp[0] == 'h'):
            max = guess
        elif (resp[0] == 'l'):
            min = guess
        elif (resp[0] == 'c'):
            print(f"Game over. Your secret number was: {guess}")
            break
        else:
            print("Sorry, I did not understand your input.  Please type [h  l  c]\y")


def user_guess_the_number(min, max):
    random_number = random.randint(min, max)
    print(f'\nI thought of a number between {min} and {max} inclusive {45}.  Try to guess it.')


if __name__ == '__main__':
    min = 1
    max = 100
    computer_guess_the_number(min, max)
    user_guess_the_number(min, max)
