"""
Implement popular game: Tic Tac Toe
Reference: Kylie Ying: @kylieyying : https://www.youtube.com/watch?v=8ext9G7xspg 
With minor modifications to improve readability.
"""

import gm_tic_tac_toe_player as tttp

class TicTacToe:
    def __init__(self):
        self.wide: int = 3
        self.high: int = 3
        self.board = [' ' for _ in range(9)]        # Build a 3x3 board
        self.current_winner = None                  # Track any current winner

    def print_board(self) -> None:
        print()
        for row in [self.board[i*3 : (i+1)*3] for i in range(self.wide)]:
            print('|' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        """
        Print board with numbers for each position for player to choose their move.
        Expected to be called only once at start of game.  0 | 1 | 2 ... (tells us what number
        corresponds to what box on the board).  Note: This is a staticmethod, so we're NOT
        passing "self".  It's the same board for both players.
        40:00 min into video.
        """
        print()
        # Build a board of size [_sz_board x _sz_board]
        _sz_board = 3
        number_board = [[str(col*_sz_board + row) for row in range(_sz_board)] for col in range(_sz_board)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        print()

    def available_moves(self) -> list:
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o] -> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':     # empty space
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        # return len(self.available_moves())
        return self.board.count(' ')

    def make_move(self, posn: int, letter: str):
        if self.board[posn] == ' ':       # This spot is available
            self.board[posn] = letter
            if self.winner(posn, letter):     # Did I just win?
                self.current_winner = letter
            return True
        return False

    def winner(self, posn: int, letter: str) -> bool:
        """ winner if there's 3 in a row anywhere: rows, cols, diagonals ... """
        # check the rows for a winner
        row_ind = posn // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check the cols for a winner
        col_idx = posn % 3
        col = [self.board[col_idx + i*3] for i in range(self.high)]
        if all([spot == letter for spot in col]):
            return True

        # check diagonals if posn is in [0, 2, 4, 6, 8]
        if posn % 2 == 0:
            tl_br = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in tl_br]):
                return True
            tr_bl = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in tr_bl]):
                return True

        return False

def play(ttt: TicTacToe, x_player, o_player):
    """ return the winner's letter, or None for a tie """

    ttt.print_board_nums()

    letter = 'X'        # starting letter
    # iterate while available empty squares.  Break when there's a winner.
    while ttt.empty_squares():
        posn = o_player.get_move(ttt) if letter == 'O' else  x_player.get_move(ttt)

        if ttt.make_move(posn, letter):
            print(letter + f' makes a move to square {posn}')
            ttt.print_board()      # print updated board
            print()

        if ttt.current_winner:     # someone won the ttt!
            print(letter + ' wins!\n')
            return letter

        letter = 'O' if letter == 'X' else 'X'      # other player's turn

    print("It's a tie ...")
    return None


if __name__ == '__main__':
    x_player = tttp.HumanPlayer('X')
    o_player = tttp.RandomComputerPlayer('O')
    ttt = TicTacToe()
    play(ttt, x_player, o_player)
