import unittest
import pygame
from cells import Cells
from global_values import *

class TestCells(unittest.TestCase):
    '''
    Args:
    '''

    def test_cell_value_when_all_1(self):
        '''
        All cells blocked
        '''
        cells = Cells(SCREEN_HEIGHT, SCREEN_WIDTH, CELL_SIZE, 1)
        first = cells.cell_value(1, 1)
        second = cells.cell_value(100, 100)
        third = cells.cell_value(2, 231)
        self.assertEqual(first, 1)
        self.assertEqual(second, 1)
        self.assertEqual(third, 1)

    def test_cell_value_if_weird(self):
        '''
        Out of bounds inputs
        '''
        cells = Cells(SCREEN_HEIGHT, SCREEN_WIDTH, CELL_SIZE, 1)
        first = cells.cell_value(-1, -1)
        second = cells.cell_value(100000, 100000)
        self.assertEqual(first, 1)
        self.assertEqual(second, 2)
