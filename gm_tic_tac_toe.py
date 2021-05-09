""" Implement popular game: Tic Tac Toe """

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

    def available_moves(self) -> array:
        return [i for i, spot in enumerate(self.board) if spot = ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o] -> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':     # empty space
        #         moves.append(i)
        # return moves

ttt: TicTacToe = TicTacToe()
ttt.print_board()
ttt.print_board_cur()
