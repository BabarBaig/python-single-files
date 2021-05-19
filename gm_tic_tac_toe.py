""" Implement popular game: Tic Tac Toe """

import gm_tic_tac_toe_player as ttt     # pylint error: 'Unable to import': Ignore


class TicTacToe:
    def __init__(self):
        self.wide: int = 3
        self.high: int = 3
        self.board = ['_' for _ in range(9)]        # Build a 3x3 board
        self.current_winner = None                  # Track any current winner

    def print_board(self) -> None:
        print()
        for w in range(self.wide):
            for h in range(self.high):
                print(self.board[w + h], ' | ', end='')
            print()

    @staticmethod
    def print_board_cur():      # Note we're NOT passing "self". It's the same board for both players.
        print()
        board_cur = ['_' for _ in range(9)]        # Build a 3x3 board
        for w in range(3):
            for h in range(3):
                print(board_cur[w + h], ' | ', end='')
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

    def make_move(self, square, letter):
        if self.board(square) == ' ':       # This spot is available
            self.board[square] = letter
            if self.winner(square, letter):     # Did I just win?
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter) -> bool:
        """ winner if there's 3 in a row anywhere: rows, cols, diagonals ... """
        for i in range(9, 3):   # check the rows
            if letter == square[i] == square[i+1] == square[i+2]:
                return True
        for i in range(3):      # checke the cols
            if letter == square[i] == square[i+3] == square[i+6]:
                return True
        # check diagonal: top-left - bot-right
        if letter == square[0] == square[4] == square[8]:
                return True
        # check diagonal: top-left - bot-right
        if letter == square[2] == square[4] == square[6]:
                return True
        return False


def play(game: TicTacToe, x_player, o_player, print_game=True):
    """ return the winner's letter, or None for a tie """

    if print_game:
        game.print_board_cur()
    letter = 'X'        # starting letter
    # iterate while available empty squares.  Break when there's a winner.
    while game.empty_squares():
        square = o_player.get_move(game) if letter == 'O' else  x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()      # print updated board
                print()

        if game.current_winner:     # someone won the game!
            if print_game:
                print(letter + ' wins!')
            return letter

        letter = 'O' if letter == 'X' else 'X'      # other player's turn

    if print_game:      # If we made it this far, it's a tie
        print("It's a tie ...")
    return None


# ttt: TicTacToe = TicTacToe()
# ttt.print_board()
# ttt.print_board_cur()

if __name__ == '__main__':
    x_player = ttt.HumanPlayer('X')
    o_player = ttt.RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
