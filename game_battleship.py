"""
#-------------------------------------------------------------------------------
# Name:        gm_battleship.py
# Purpose:     Game: Create a square game board sz_board in size.
#              Hide a battleship somewhere on the board
#              Give user num_tries to guess where the ship is hiding
#
# Author:      Baig-Admin
#
# Created:     05/01/2013
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""

import random


def create_board(sz_board1):
    rows, cols = (sz_board1, sz_board1)
    board = [['O' for i in range(cols)] for j in range(rows)]
    return board


def print_board(board1):
    print()
    for row in board1:          #Iterate over each row in board[]
        print(" ".join(row))    #Concat all 'O's, separate by a space


def battleship_game():
    board_sz = 5
    print("\nLet's play Battleship!  Guess my ship's location to sink it!")
    board = create_board(board_sz)
    print_board(board)

    ship_row = random.randint(1, board_sz)
    ship_col = random.randint(1, board_sz)
    print(f'\n\tShip location: [{ship_row}, {ship_col}]')
    turn_max = 6

    for turn in range(turn_max):
        print_board(board)
        print(f'Lives remaining {turn_max - turn}')
        prompt = "Guess Row: [1 - " + str(board_sz) + "]\t"
        guess_row = int(input(prompt))
        prompt = "Guess Col: [1 - " + str(board_sz) + "]\t"
        guess_col = int(input(prompt))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        elif guess_row < 1 or guess_row > board_sz or guess_col < 1 or guess_col > board_sz:
            print("Oops, that's not even in the ocean.")
        elif board[guess_row-1][guess_col-1] == 'X':
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row-1][guess_col-1] = 'X'

    print("Game Over")


if __name__ == '__main__':
    battleship_game()
