""" Implement popular ttt: Tic Tac Toe """

import gm_tic_tac_toe_player as tttp
# from . import gm_tic_tac_toe_player as tttp
# from ..aaa_py_simple import gm_tic_tac_toe_player as tttp

class TicTacToe:
    def __init__(self):
        self.wide: int = 3
        self.high: int = 3
        self.board = [' ' for _ in range(9)]        # Build a 3x3 board
        self.current_winner = None                  # Track any current winner

    def print_board(self) -> None:
        print()
        for w in range(self.wide):
            for h in range(self.high):
                print(self.board[w + h], ' | ', end='')
            print()

    @staticmethod
    def print_board_nums():
        """
        Print board with numbers for each position for player to choose their move.
        0 | 1 | 2 ... (tells us what number corresponds to what box on the board)
        Note: This is a staticmethod, so we're NOT passing "self".
        It's the same board for both players.
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
        for i in range(9, 3):   # check the rows
            if letter == self.board[i] == self.board[i+1] == self.board[i+2]:
                return True
        for i in range(3):      # checke the cols
            if letter == self.board[i] == self.board[i+3] == self.board[i+6]:
                return True
        # check diagonal: top-left - bot-right
        if letter == self.board[0] == self.board[4] == self.board[8]:
                return True
        # check diagonal: top-left - bot-right
        if letter == self.board[2] == self.board[4] == self.board[6]:
                return True
        return False


def play(ttt: TicTacToe, x_player, o_player, print_ttt=True):
    """ return the winner's letter, or None for a tie """

    if print_ttt:
        ttt.print_board_nums()

    letter = 'X'        # starting letter
    # iterate while available empty squares.  Break when there's a winner.
    while ttt.empty_squares():
        square = o_player.get_move(ttt) if letter == 'O' else  x_player.get_move(ttt)

        if ttt.make_move(square, letter):
            if print_ttt:
                print(letter + f' makes a move to square {square}')
                ttt.print_board()      # print updated board
                print()

        if ttt.current_winner:     # someone won the ttt!
            if print_ttt:
                print(letter + ' wins!')
            return letter

        letter = 'O' if letter == 'X' else 'X'      # other player's turn

    if print_ttt:      # If we made it this far, it's a tie
        print("It's a tie ...")
    return None


if __name__ == '__main__':
    x_player = tttp.HumanPlayer('X')
    o_player = tttp.RandomComputerPlayer('O')
    ttt = TicTacToe()
    play(ttt, x_player, o_player, print_ttt=True)
