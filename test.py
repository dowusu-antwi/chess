#!/usr/bin/env python3

"""
Test Cases for Chess Game/AI
"""

import unittest
import main

def generate_default_board():
    return [['rtl','ktl','btl','Qt','Kt','btr','ktr','rtr'],
            ['pt1','pt2','pt3','pt4','pt5','pt6','pt7','pt8'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['pb1','pb2','pb3','pb4','pb5','pb6','pb7','pb8'],
            ['rbl','kbl','bbl','Qb','Kb','bbr','kbr','rbr']] 

class Test(unittest.TestCase):

    # this test verifies the default board
    #  representation
    def test_01(self):
        g = main.Game()
        result = g.display_board()
        expected = generate_default_board()
        self.assertEqual(result, expected)

    # this test checks a simple pawn move
    def test_02(self):
        g = main.Game()
        result = g.respond_to_move('pb4',(5,3))
        expected = generate_default_board()
        expected[6][3], expected[5][3] = ('', expected[6][3])
        self.assertEqual(result, expected)

if __name__ == "__main__":

    result = unittest.main(verbosity=3, exit=False)
