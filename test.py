#!/usr/bin/env python3

"""
Test Cases for Chess Game/AI
"""

import unittest
import main

generate_default_board = main.generate_default_board

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
