import random
import unittest
import pygame
from entities.cells import Cells
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
        """
        tests whether changing cells works
        """
        cells = Cells(0)
        size_x = tower1['size_y']
        size_y = tower1['size_x']
        rand_x = random.randint(0, SCREEN_WIDTH-1)
        rand_y = random.randint(0, SCREEN_HEIGHT-1)
        tower_rect = pygame.Rect(rand_x, rand_y, size_x, size_y)
        cells.change_cells_to(rand_x, rand_y, tower_rect, 1)
        cell_val = cells.cell_value(rand_x, rand_y)
        self.assertEqual(cell_val, 1)

    def test_change_cells_to_2(self):
        cells = Cells(0)
        size_x = tower1['size_y']
        size_y = tower1['size_x']
        x_pos = 762
        y_pos = 572
        tower_rect = pygame.Rect(x_pos, y_pos, size_x, size_y)
        cells.change_cells_to(x_pos, y_pos, tower_rect, 1)
        cell_val = cells.cell_value(x_pos, y_pos)
        self.assertEqual(cell_val, 1)

    def test_get_neighbours(self):
        """
        checks that the system returns correct amount of neighbours
        """
        cells = Cells(0)
        neibs = cells.get_neighbours((0, 0))
        self.assertEqual(len(neibs), 2)
        neibs2 = cells.get_neighbours((100, 100))
        self.assertEqual(len(neibs2), 4)

    def test_coords_to_cell_values(self):
        """
        .
        """
        cells = Cells(0)
        x_1, y_2 = cells.coords_to_cell_values(0, 0)
        self.assertEqual(x_1, 0)
        self.assertEqual(y_2, 0)

    def test_coords_to_cell_values2(self):
        """
        .
        """
        cells = Cells(0)
        x_1, y_2 = cells.coords_to_cell_values(-1, -1)
        self.assertEqual(x_1, 0)
        self.assertEqual(y_2, 0)

    def test_coords_to_cell_values3(self):
        """
        .
        """
        cells = Cells(0)
        more = SCREEN_WIDTH + SCREEN_HEIGHT
        x_1, y_2 = cells.coords_to_cell_values(more, more)
        self.assertEqual(x_1, len(cells.cells[0])-1)
        self.assertEqual(y_2, len(cells.cells)-1)
