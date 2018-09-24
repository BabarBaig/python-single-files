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

import random

def main():
    pass

if __name__ == '__main__':
    main()

def create_board(sz_board1):
    board1 = []
    for count in range (sz_board1):
        board1.append(['O']*5) #Add 1 element in board1--a list with 5 elements
    return board1

def print_board(board1):
    for row in board1:          #Iterate over each row in board[]
        print(" ".join(row))    #Concat all 'O's, separate by a space

def random_row(board1):
    row_idx_max = len(board1) - 1
    return random.randint(0, row_idx_max)

def random_col(board1):
    col_idx_max = len(board[0]) - 1
    return random.randint(0, col_idx_max)

board_sz=5
board_idx_max = board_sz-1
board_idx_max_str = str(board_idx_max)
board = create_board(board_sz)
print("Let's play Battleship!")
print_board(board)
ship_row = random_row(board)
ship_col = random_col(board)
turn_max=4
for turn in range(turn_max):
    guess_row = int(input("Guess Row [0-:"+board_idx_max_str+"]:"))
    guess_col = int(input("Guess Col [0-:"+board_idx_max_str+"]:"))
    print(ship_col)
    print(ship_row)
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row<0 or guess_row>board_idx_max) or \
           (guess_col<0 or guess_col>board_idx_max):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col]=='X':
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = 'X'
            print_board(board)
    print(turn+1)
    if turn+1==turn_max:
        print("Game Over")
#