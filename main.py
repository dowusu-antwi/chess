#!/usr/bin/env python3

"""
Simple Chess AI
author: dowusu
"""

def generate_default_board():
    # key: rtl -> rook-top-left
    return [['rt','kt','bt','Qt','Kt','bt','kt','rt'],
            ['pt','pt','pt','pt','pt','pt','pt','pt'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['pb','pb','pb','pb','pb','pb','pb','pb'],
            ['rb','kb','bb','Qb','Kb','bb','kb','rb']]

def map_moves_to_positions(width, height):
    """
    This will create a dictionary of lists mapping
     moves to positions on the board; currently, max
     board dimensions are [26,10] (letters by numbers)
    """

    alph, nums = 'abcdefghijklmnopqrstuvwxyz', '87654321'
    move_position_mapping = {alph[column]+nums[row]: (row, column) for row in range(height) for column in range(width)}
    position_move_mapping = {(row, column):alph[column]+nums[row] for row in range(height) for column in range(width)}
    return move_position_mapping, position_move_mapping

class Player:

    def __init__(self):
        pass

    def send_move(self):
        pass

class Game:

    def __init__(self):

        width, height = 8, 8

        self.board = generate_default_board()
        self.moves_mapped_to_positions, self.positions_mapped_to_moves = map_moves_to_positions(width, height)
        self.width, self.height = width, height

        self.moves = {
          'bishop': self.get_diagonal,
          'rook': lambda position: self.get_horizontal(position) | self.get_vertical(position),
          'queen': lambda position: self.get_horizontal(position) | self.get_vertical(position) | self.get_diagonal(position),
          'knight': lambda position: self.get_positions(position, 'knight'),
          'pawn': lambda position: self.get_positions(position, 'pawn'),
          'king': lambda position: self.get_position(position, 'king')
         }
        self.move_constants = {
          'knight': {(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)},
          'pawn': {'top': {(1,0)}, 'bottom': {(-1,0)}},
          'king': {(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)}
         }

    def in_bounds(self, position):
        """
        This returns True if the given position is in the bounds
         of the board, False otherwise
        """
        row, col = position
        return ((row >= 0 and row <= self.height) and
                (col >= 0 and col <= self.width))

    def respond_to_move(self, move):
        """
        This will respond to a move (a tuple with the old position
         and the new position to move to, in algebraic notation,
         i.e., 7th row, 0th column -> 'a1'
        """

        # this will get the piece at the queried position,
        #  will notify user if there is no piece there
        current_algebraic, new_algebraic = move
        row, column = self.moves_mapped_to_position[current_algebraic]
        piece = self.board[row][column]
        if piece == '':
            print("There is no piece at %s" % current_algebraic)
            return

        # this will get all possible moves from this position
        #  and will make the move if the new position is a
        #  valid move
        piece_name = piece_names[piece]
        moves = self.moves[piece_name][(row, column)]
        
        new_row, new_column = self.moves_mapped_to_position[new_algebraic]
        if (new_row, new_column) in moves:
            # this will change the game board to reflect the move
            self.game_board[row][column]  = piece
            self.game_board[new_row][new_column] = piece

    def display_board(self):
        """
        This will return the list representing the chess board
        """
        return self.board

    def get_upper_diagonal(self, position):

        print("position:",position)
        row, col = position
        new_position = (row+1, col+1)
        print("new position:",new_position)
        if self.in_bounds(new_position):
            return {new_position} | self.get_upper_diagonal(new_position)
        return set()


    def get_lower_diagonal(self, position):

        row, col = position
        new_position = (row-1, col-1)
        if self.in_bounds(new_position):
            return {new_position} | self.get_lower_diagonal(new_position)
        return set()

    def get_diagonal(self, position):
        """
        This will get all positions diagonal
         from the given position
        """

        upper = self.get_upper_diagonal(position)
        lower = self.get_lower_diagonal(position)
        return upper | lower

    def get_horizontal(self, position):
        """
        This will get all positions horizontal
         to the given position
        """
        pass

    def get_vertical(self, position):
        pass

if __name__ == "__main__":

    g = Game()
    print(g.get_diagonal((0,1)))
