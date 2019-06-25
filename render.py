#!/usr/bin/env python3

"""
Chess-AI Renderer
author: dowusu

This will use PyQt to render the chess board
 to the screen
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
import sys

class App(QtWidgets.QWidget):
    """
    This is the main 'widget' class
    """

    def __init__(self, window_dimensions):
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
        width, height = window_dimensions
        self.resize_window(width, height)
        #self.timer = self.setup_timer()

        ########################################
        # draw an image to the screen
        label = QLabel(self) 
        pixmap = QPixmap('sprites/w_queen.png')
        label.setPixmap(pixmap)
        label.setGeometry(0,0,pixmap.width(),pixmap.height())
        ########################################

        # this keeps track of whether rendering
        #  has begun, first frame is skipped
        #  automatically so rendering starts
        #  after the first frame
        self.drawn = None

        # this opens the hidden PyQt window, showing
        #  it on the screen
        self.show()

    def resize_window(self, width, height):
        """
        This resizes the application window.
        """
        self.setGeometry(0,0,width,height)


    def draw_rectanlges():
        """
        """
        pass

    def draw_objects():
        """
        """
        pass

    def paintEvent(self, event):
        """
        This method paints elements to the screen, as
         given by PyQt
        """
        pass

if __name__ == "__main__":

    new_app = App([400, 400])
    # app.exec_() runs main app loop, ret status code
    #  upon exit; sys.exit passes on status code to
    #  parent process (i.e., the shell), so that if
    #  program errors out it can be detected...
    sys.exit(new_app.qapp.exec_())
