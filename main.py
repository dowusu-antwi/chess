#!/usr/bin/env python3

"""
Simple Chess AI
author: dowusu
"""

class Player:

    def __init__(self):
        pass

class Game:

    def __init__(self):

        self.move_constants =
         {'knight': {(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)},
          'pawn': {'top': {(1,0}}, 'bottom': {(-1,0)}},
          'king': {(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)}
         }

        self.moves =
         {'bishop': get_diagonal,
          'rook': lambda position: get_horizontal(position) | get_vertical(position),
          'queen': lambda position: get_horizontal(position) | get_vertical(position) | get_diagonal(position),
          'knight': lambda position: get_positions(position, 'knight'),
          'pawn': lambda position: get_positions(position, 'pawn'),
          'king': lambda position: get_position(position, 'king')
         }

    def get_diagonal(self, position):
        """
        This will get all positions diagonal
         from the given position
        """
        pass

    def get_horizontal(self, position):
        """
        This will get all positions horizontal
         to the given position
        """
        pass

    def get_vertical(self, position):
        pass

if __name__ == "__main__":


