import unittest
from pf.astar import Astar
from cells import Cells
from global_values import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE

class TestAstar(unittest.TestCase):
    """
    Tests for astar class
    """

    def test_path_in_one_cell_wide_system(self):
        """
        Test if astar can find path in 1 cell wide system
        """
        pass
        #cells = Cells(0, 5, 100, 5)
        #astar = Astar()
        #came_from, cost_so_far = astar.search(cells, (0, 0), (100, 100))

