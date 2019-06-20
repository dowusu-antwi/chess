#!/usr/bin/env python3

"""

"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

class App(QtWidgets.QWidget):
    """
    This is the main 'widget' class
    """

    def __init__(self, window_dimensions):
        # this creates a QApplication object, passing
        #  in sys.argv to allow for passing of cmd line
        #  args to self.app
        #
        # the app method exec_() is called later to
        #  start running the application

        self.app = QApplication(sys.argv)
        
        # super(Class, object).__init__() - this calls
        #  the init method of the object's parent class,
        #  can be written super().__init__() since py3
        super().__init__()

        self.setWindowTitle("Chess")
        width, height = window_dimensions
        self.resize_window(width, height)
        #self.timer = self.setup_timer()

        # this keeps track of whether rendering
        #  has begun, first frame is skipped
        #  automatically so render starts after
        #  the first frame
        self.drawn = None

    def resize_window(self, width, height):
        """
        This resizes the application window.
        """
        pass

if __name__ == "__main__":


