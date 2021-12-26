import unittest
from pf.astar import Astar
from pf.pathfinding import Pathfind
from cells import Cells
from global_values import CELL_SIZE

class TestPathfind(unittest.TestCase):
    """
    Tests for Pathfind class
    """

    def test_path_in_one_cell_wide_system(self):
        """
        does pf find path in 1 cell wide system
        """
        cells = Cells(0, CELL_SIZE, 100, CELL_SIZE)
        astar = Astar()
        pather = Pathfind(cells, astar)
        path = pather.calc_path((0, 0), (99, 0))
        self.assertEqual(len(path), 100/CELL_SIZE)

