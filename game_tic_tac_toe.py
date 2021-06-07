
class TicTacToe:
    def __init__(self):
        self.wide: int = 3
        self.high: int = 3
        self.board = ['_' for _ in range(9)]

    def print_board(self) -> None:
        for w in range(self.wide):
            for h in range(self.high):
                print(self.board[w + h], ' | ', end='')
            print()

ttt: TicTacToe = TicTacToe()
ttt.print_board()
