# Unit 1 Homework 9000 Test script
# Author: Chris Proctor and Jacob Wolf
# --------------------
# YOU DO NOT NEED TO UNDERSTAND THIS CODE RIGHT NOW!
# This script imports all the functions from your homework and tests them out. Hopefully they work!
# Testing is really important in computer science, so some nice functions are provided. We'll use them.

import unittest

from hw_01_06 import *

class TestHomework_01_06(unittest.TestCase):

    def test_line_y_value(self):
        self.assertEqual(line_y_value(2, .5, 1), 2)
        self.assertEqual(line_y_value(0, .3, 4), 4)
        self.assertEqual(line_y_value(2, 1, 4), 6)
        self.assertEqual(line_y_value(2, -1, 4), 2)
        self.assertEqual(line_y_value(2, -4, 4), -4)
        self.assertEqual(line_y_value(-2, .5, 2), 1)


    def test_residual(self):
        self.assertEqual(y_distance((1,2), 0.5, 2), 0.5)
        self.assertEqual(y_distance((1,3), 0.5, 2), 0.5)
        self.assertEqual(y_distance((3,3), 0.0, 3), 0.0)
        self.assertEqual(y_distance((-1,-2), 0.5, 2), 3.5)
        self.assertEqual(y_distance((-1,-2), 0.5, 2), 3.5)


    def test_closest_to_line(self):
        self.assertEqual(closest_to_line([(0,0), (2,3.5)], 1, 1), (2,3.5))
        self.assertTrue(closest_to_line([(0,0), (1,1), (2,2)], 1, 0) == (0,0) or (1,1) or (2,2))
        self.assertEqual(closest_to_line([(1,100000)], 1, 1), (1, 100000))
        self.assertTrue(closest_to_line([(-1,2), (1,2), (1, -2), (-1, -2)], 0, 1) == (-1,-2) or (-1,2) or (1,2))


# This runs all the tests.
unittest.main()
