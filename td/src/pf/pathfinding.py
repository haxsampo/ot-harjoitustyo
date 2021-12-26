import pygame
from global_values import CELL_SIZE

class Pathfind:
    """
    Holds pathfinding functions, to now clutter level
    """

    def __init__(self, cells, algo):
        self.cells = cells
        self.algo = algo

    def calc_path(self, start, end):
        """
        Calculates path for enemies
        Return:
        If succesful returns a list of tuples that are top left corners of cells that mark the path
        if unsuccesful (path blocked), returns False
        """
        start = (start[0] - (start[0] % CELL_SIZE), start[1] - (start[1] % CELL_SIZE))
        end = (end[0] - (end[0] % CELL_SIZE), end[1] - (end[1] % CELL_SIZE))
        came_from, cost_so_far = self.algo.search(self.cells, start, end)
        path_ok = self._path_exists(came_from, end)
        if not path_ok:
            return False
        cleaned_path = self.clean_path(start, end, came_from)
        return cleaned_path

    def _path_exists(self, came_from, end):
        """
        Estimates whether the pf algo couldn't find a path to base
        Args:
        came_from (dict): from self.algo.search()
        """
        if end not in came_from:
            return False
        if len(came_from) == 1 and None in list(came_from.values()):
            return False
        else:
            return True

    def clean_path(self, start, end, path_dict):
        """
        cleans the path dictionary into a list, start as first index and end as last
        """
        path_list = []
        curr = end
        while curr != start:
            path_list.append(curr)
            curr = path_dict[curr]
        path_list.append(start)
        rev = list(reversed(path_list))
        return rev

    def update_paths(self, enemies, end):
        """
        Updates the path for all enemies in level
        """
        for enemy in enemies:
            x_pos = int(enemy.rect.x - (enemy.rect.x % CELL_SIZE))
            y_pos = int(enemy.rect.y -(enemy.rect.y % CELL_SIZE))
            new_path = self.calc_path((x_pos, y_pos), end)
            if not new_path:
                return
            enemy.path = new_path
            enemy.path_index = 0

    def force_path_find(self,x_pos, y_pos, new_path, end):
        """
        force new pathing if pathing resolves no none
        """
        for i in range(10):
            if not new_path:
                new_path = self.calc_path((x_pos, y_pos), end)
        return new_path
