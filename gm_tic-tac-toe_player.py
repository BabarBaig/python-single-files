"""
Implement player class for popular game: Tic Tac Toe
"""

import math
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
        square = random.choice()


class HumanPlayer(Player):
    def __init__(self, letter):
        super.__init__(letter)

    def get_move(self, game):
        pass
