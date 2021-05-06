<<<<<<< HEAD
import sys

def guess_a_number(min, max):
    min = 0
    max = 100
    print('Please think of a number between 0 and 100!')
    guess = (min + max)/2
    while(1):
        print('Is your secret number {0}?' .format(guess))
        your_resp = raw_input('Enter \'h\' to indicate the guess is too high.  '+
                              'Enter \'l\' to indicate the guess is too low.  '+
                              'Enter \'c\' to indicate I guessed correctly: ')
        if (your_resp[0] == 'h'):
            guess_a_number(min, guess)
            break
        elif (your_resp[0] == 'l'):
            guess_a_number(guess, max)
            break
        elif (your_resp[0] == 'c'):
            print("Game over. Your secret number was: {0}" .format(guess))
            break
        else:
            print("Sorry, I did not understand your input.")

if __name__ == '__main__':
    guess_a_number(0, 100)
=======
import sys

def guess_a_number(min, max):
    min = 0
    max = 100
    print('Please think of a number between 0 and 100!')
    guess = (min + max)/2
    while(1):
        print('Is your secret number {0}?' .format(guess))
        your_resp = raw_input('Enter \'h\' to indicate the guess is too high.  '+
                              'Enter \'l\' to indicate the guess is too low.  '+
                              'Enter \'c\' to indicate I guessed correctly: ')
        if (your_resp[0] == 'h'):
            guess_a_number(min, guess)
            break
        elif (your_resp[0] == 'l'):
            guess_a_number(guess, max)
            break
        elif (your_resp[0] == 'c'):
            print("Game over. Your secret number was: {0}" .format(guess))
            break
        else:
            print("Sorry, I did not understand your input.")

if __name__ == '__main__':
    guess_a_number(0, 100)
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
