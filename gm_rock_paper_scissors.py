""" 2021-06-13: Program works """

import random


def play():
    user = input("Choose [(r)ock  (p)aper  (s)cissors, (q)uit]:\t")
    computer = random.choice(['r', 'p', 's'])

    if user == 'q':
        return user

    if user == computer:
        return "It's a tie"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'Computer chose [' + computer + '].  You won!'

    return 'Computer chose [' + computer + '].  You lost!'


def is_win(player, opponent):
    """ r > s, s > p, p > r
    return true if player wins """

    if player == 'r' and opponent == 's':   return True
    if player == 's' and opponent == 'p':   return True
    if player == 'p' and opponent == 'r':   return True
    return False


while (retval := play()) != 'q':
    print(retval)
print('\n')
