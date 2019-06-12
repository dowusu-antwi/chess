#!/usr/bin/env python3

"""
Simple Chess AI
author: dowusu
"""

def generate_default_board():
    return [['rtl','ktl','btl','Qt','Kt','btr','ktr','rtr'],
            ['pt1','pt2','pt3','pt4','pt5','pt6','pt7','pt8'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['pb1','pb2','pb3','pb4','pb5','pb6','pb7','pb8'],
            ['rbl','kbl','bbl','Qb','Kb','bbr','kbr','rbr']]

class Player:

    def __init__(self):
        pass

class Game:

    def __init__(self):

        self.board = generate_default_board() 

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

    def respond_to_move(self, move):
        pass

    def display_board(self):
        return self.board

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

    pass
