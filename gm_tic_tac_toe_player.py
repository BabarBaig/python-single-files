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
        super().__init__(letter)

    def get_move(self, game) -> int:
        """ Get a random spot on the board """
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter) -> int :
        super().__init__(letter)

    def get_move(self, game) -> int:
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn.  Input move [0-8]:\t')
            # Error if value is not an int, or spot not available on the board
            try:
                if (value := int(square)) not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square!  Try again')
        return value


class GeniusComputerPlayer(Player):
    def __init_(self, letter):
        super().__init__(letter)

    def get_move(self, game) -> int:
        if len(game.available_moves()) == 9:                    # blank board
            posn = random.choice(game.available_moves())        # choose a random spot
        else:
            # recursion: get a position based on the minimax algorithm
            posn = self.minimax(game, self.letter)['position']
        return posn

    def minimax(self, state, player):
        max_player = self.letter                            # yourself!
        oth_player = 'O' if player == 'X' else 'X'          # other player

        # recursion requires a base case:
        if state.current_winner == oth_player:              # first check if previous move was a winner
            score = state.empty_squares() + 1            # return position AND scrore--need for minmax to work
            if oth_player ==  max_player: pass              # we already have correct score
            else: score = -score
            return {'position': None, 'score': score }      # position: None b/c we didn't move
        elif not state.empty_squares():                     # it's a draw
            return {'position': None, 'score': 0}           # position: None b/c we didn't move

        # now we're past the base cases
        if player == max_player:
            best = {'position': None, 'score': -math.inf}   # each score should MAXIMIZE (be larger)
        else:
            best =  {'position': None, 'score': math.inf}   # each score should MINIMIZE
        
        for possible_move in state.available_moves():
            # 1] make a move, try that spot
            state.make_move(possible_move, player)

            # 2] recurse using minimax to simulate a game after making that move
            simulated_score = self.minimax(state, oth_player)      # we switch players

            # 3] undo that move so we can try other options
            state.board[possible_move] = ' '
            state.current_winner = None                     # undo hypothetical move
            simulated_score['position'] = possible_move     # need this for recursion

            # 4] update the dictionaries IF NECESSARY:
            #        possible move tried, had a higher score than current best score > update!
            if player == max_player:                        # we're trying to maximize max_player
                if simulated_score['score'] > best['score']:
                    best = simulated_score                  # update best score
            else:                                           # We're trying to minimize the other player
                if simulated_score['score'] < best['score']:
                    best = simulated_score                  # update best score

        return best
