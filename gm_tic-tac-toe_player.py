"""
Implement player class for popular game: Tic Tac Toe
"""

# import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter        # letter should be X or O

    def get_move(self):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super.__init__(letter)

    def get_move(self, game):
        """ Get a random spot on the board """

        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super.__init__(letter)

    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn.  Input move [0-9]:\t')
            # Error if value is not an int, or spot not available on the board
            try:
                if (value := int(square)) not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square!  Try again')
        return value
