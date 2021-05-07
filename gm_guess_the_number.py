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
    print(f'\nI thought of a number between {min} and {max} inclusive {random_number}.  Try to guess it.')
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between {min} and {max} inclusive:\t'))
        if guess < random_number:
            print('Sorry, guess again.  Too low.')
        elif guess > random_number:
            print('Sorry, guess again.  Too high.')
        else:
            print(f'Success!  You guessed the number {random_number}.')


if __name__ == '__main__':
    min = 1
    max = 100
    computer_guess_the_number(min, max)
    user_guess_the_number(min, max)
