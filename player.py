import math

import random


class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
           #takes in human input, returns it into the integer n return that value
           square = input(self.letter + '\'s turn, Input move (0-9): ')
           try:
               val = input(square)
               if val not in game.avaliable_moves():
                   raise ValueError
               valid_square = True
           except ValueError:
                print('Invalid square. Try again.')
        return val


# this type of player just sees what square is avaliable on the board
class RandomPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
         square = random.choice(game.avaliable_moves())
         return square



class SmartComputerPlayer(Player):
        def __init__(self, letter):
            super().__init__(letter)

        def get_move(self, game):
            # if its an empty game it randomly chooses somewhere to go
            if len(game.available_moves()) == 9:
                square = random.choice(game.available_moves())
            else:
                #otherwise uses minimax algorithm in order to generate the smartest possible choice at that moment
                square = self.minimax(game, self.letter)['position']
            return square  

