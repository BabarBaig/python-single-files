# Using a guess_number game to show good OOP
# Tech With Tim
# https://www.youtube.com/watch?v=-njsRb8Tn70

# from aaa_hello import guess_number      # correct format even though PyLink flags an error

# def guess_number():
#     GUESS = 45
#     MIN = 1
#     MAX = 100
#     count = 0
#     while(True):
#         count += 1
#         num = input("Please guess the number [1 - 100]:\t")
#         try:
#             num = int(num)
#         except:
#             print ('Invalid number, please guess again.')
#             continue

#         if num < GUESS:
#             print('Your guess was low!')
#         elif num > GUESS:
#             print('Your guess was high!')
#         else:       # guessed!
#             break

#     print(f'You guessed correctly in {count} tries!')

import sys

class GuessANumber():
    def __init__(self, guess:int, min:int = 1, max:int = 100):
        self.guess = guess
        self.min = min
        self.max = max
        self.count = 0

    def get_valid_guess(self):
        while(True):
            num = input(f"Please guess the number ({self.min} - {self.max})[Quit]:\t")
            if num == 'q':
                sys.exit(0)
            try:
                num = int(num)
            except:
                print ('Invalid number, please guess again.')
                continue

            if (num < self.min or num > self.max):
                print(f'Your guess {num} is out of range!')
                continue

            return num

    def play(self):
        while(True):
            num = self.get_valid_guess()
            self.count += 1
            if num < self.guess:
                print('Your guess was low!')
            elif num > self.guess:
                print('Your guess was high!')
            else:       # guessed!
                break

        print(f'You guessed correctly in {self.count} tries!\n')

gan = GuessANumber(45)
gan.play()
