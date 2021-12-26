import unittest
import pygame
import random
from cells import Cells
from global_values import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE
from tower_values import tower1

class TestCells(unittest.TestCase):
    """
    Args:
    """

    def test_cell_value_when_all_1(self):
        """
        All cells blocked
        """
        cells = Cells(1)
        first = cells.cell_value(1, 1)
        second = cells.cell_value(100, 100)
        third = cells.cell_value(2, 231)
        self.assertEqual(first, 1)
        self.assertEqual(second, 1)
        self.assertEqual(third, 1)

    def test_cell_value_if_weird(self):
        """
        Out of bounds inputs
        """
        cells = Cells(1)
        first = cells.cell_value(-1, -1)
        second = cells.cell_value(100000, 100000)
        self.assertEqual(first, 1)
        self.assertEqual(second, 1)

    def test_cell_value_if_ok(self):
        """
        Ok inputs with random values
        """
        cells = Cells(0)
        rand_x = random.randint(0, SCREEN_WIDTH)
        rand_y = random.randint(0, SCREEN_HEIGHT)
        cell_value1 = cells.cell_value(rand_x, rand_y)
        self.assertEqual(cell_value1, 0)

    def test_cell_value_in_cells(self):
        """
        Give value in cell numbers, not pixels
        """
        cells = Cells(0)
        rand_x = random.randint(1, SCREEN_WIDTH/CELL_SIZE-1)
        rand_y = random.randint(1, SCREEN_HEIGHT/CELL_SIZE-1)
        cell_value1 = cells.cell_value_in_cells(rand_x, rand_y)
        self.assertEqual(cell_value1, 0)

    def test_tower_fits(self):
        """
        Tests the tower_fits function
        """
        cells = Cells(0)
        size_x = tower1['size_y']
        size_y = tower1['size_x']
        rand_x = random.randint(1, SCREEN_WIDTH/CELL_SIZE-1) 
        rand_y = random.randint(1, SCREEN_HEIGHT/CELL_SIZE-1)
        tower_rect = pygame.Rect(rand_x, rand_y, size_x, size_y)
        fits = cells.tower_fits(rand_x, rand_y, tower_rect)
        self.assertEqual(fits, True)

    def test_tower_fits2(self):
        """
        Tests the tower_fits function with edge values
        """
        cells = Cells(0)
        pos_x = SCREEN_WIDTH
        pos_y = SCREEN_HEIGHT
        size_x = tower1['size_y']
        size_y = tower1['size_x']
        tower_rect = pygame.Rect(pos_x, pos_y, size_x, size_y)
        fits = cells.tower_fits(pos_x, pos_y, tower_rect)
        self.assertEqual(fits, False)

    def test_change_cells_to(self):
        cells = Cells(0)
        size_x = tower1['size_y']
        size_y = tower1['size_x']
        rand_x = 799#random.randint(0, SCREEN_WIDTH) 
        rand_y = random.randint(0, SCREEN_HEIGHT)
        tower_rect = pygame.Rect(rand_x, rand_y, size_x, size_y)
        #cells.change_cells_to(rand_x, rand_y, tower_rect, 1)
        #cell_val = cells.cell_value(rand_x, rand_y)
        #self.assertEqual(cell_val, 1)
    
    def test_get_neighbours(self):
        """
        !
        """
        cells = Cells(0)
        neibs = cells.get_neighbours((0, 0))
        self.assertEqual(len(neibs), 2)
        
