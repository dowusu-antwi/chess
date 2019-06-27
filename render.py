#!/usr/bin/env python3

"""
Chess-AI Renderer
author: dowusu

This will use PyQt to render the chess board
 to the screen
"""

import main
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
import sys

class App(QtWidgets.QWidget):
    """
    This is the main 'widget' class
    """

    def __init__(self, pixel_dimensions):
        # this creates a QApplication object, passing
        #  in sys.argv to get cmd line arguments passed
        #  to the script
        #
        # the qapp method exec_() is called later to
        #  start running the application

        self.qapp = QApplication(sys.argv)
        
        # super(Class, object).__init__() - this calls
        #  the init method of the object's parent class,
        #  can be written super().__init__() since py3
        #
        # this is to get access to functions including
        #  setWindowTitle, paintEvent, setGeometry, etc.
        super().__init__()

        self.setWindowTitle("Chess")
        pixel_width, pixel_height = pixel_dimensions
        width, height = pixel_width*8, pixel_height*8
        self.resize_window(width, height)
        #self.timer = self.setup_timer()

        # this keeps track of whether rendering
        #  has begun, first frame is skipped
        #  automatically so rendering starts
        #  after the first frame
        self.drawn = None

        # this creates the game board from
        #  the main file and defines info
        #  for rendering (e.g., pixel size)
        self.game = main.Game()
        self.pixel_dimensions = pixel_dimensions
        self.pieces_mapped_to_file = {'Qb': 'w_queen.png', 'pt': 'b_pawn.png', 'pb': 'w_pawn.png',
                                      'Qt': 'b_queen.png', 'Kt': 'b_king.png', 'Kb': 'w_king.png',
                                      'rt': 'b_rook.png', 'rb': 'w_rook.png', 'bb': 'w_bishop.png',
                                      'bt': 'b_bishop.png', 'kt': 'b_knight.png', 'kb': 'w_knight.png'}

        # this opens the hidden PyQt window, showing
        #  it on the screen
        self.show()

    def resize_window(self, width, height):
        """
        This resizes the application window.
        """
        self.setGeometry(0,0,width,height)


    def draw_board(self, painter):
        """
        This will iterate over the game board and draw each
         chess square in addition to drawing each chess piece
         if one is needed
        """

        # this iterates over board, draws square
        #  then draws chess piece on top

        pixel_width, pixel_height = self.pixel_dimensions

        color = 'black'
        x_init, y_init = 0,0
        for row in self.game.board:
            
            for square in row:

                if color == 'black':
                    painter.setBrush(QtGui.QColor(40,40,40))
                elif color == 'white':
                    painter.setBrush(QtGui.QColor(255,255,255))

                painter.drawRect(x_init, y_init, x_init+pixel_width, y_init+pixel_height)

                if square in self.pieces_mapped_to_file:
                    filename = self.pieces_mapped_to_file[square]
                    pixmap = QPixmap('sprites/'+filename)
                    pixmap = pixmap.scaled(pixel_width-pixel_width//10, pixel_height-pixel_height//10)
                    painter.drawPixmap(x_init+pixel_width//20, y_init+pixel_height//20, pixmap)

                color = 'white' if color == 'black' else 'black'

                x_init += pixel_width

            color = 'white' if color == 'black' else 'black'
            x_init = 0
            y_init += pixel_height

    def draw_piece_on_square(self, painter):
        """
        """
        # prepares chess piece image
        pixmap = QPixmap('sprites/w_queen.png')

        # sets square color
        painter.setBrush(QtGui.QColor(40,40,40))

        # draws chess piece over square
        scaled_pixmap = pixmap.scaled(pixmap.width()*2, pixmap.height()*2)
        painter.drawRect(0,0,pixmap.width()*2,pixmap.height()*2)
        painter.drawPixmap(0,0,scaled_pixmap)

    def draw_objects(self, painter):
        """
        """
        #self.draw_piece_on_square(painter)
        self.draw_board(painter)

    def paintEvent(self, event):
        """
        This method paints elements to the screen, as
         given by PyQt
        """

        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw_objects(painter)
        painter.end()

if __name__ == "__main__":

    new_app = App([100, 100])
    # app.exec_() runs main app loop, ret status code
    #  upon exit; sys.exit passes on status code to
    #  parent process (i.e., the shell), so that if
    #  program errors out it can be detected...
    sys.exit(new_app.qapp.exec_())
