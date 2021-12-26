from pf.priorityqueue import PriorityQueue
from global_values import CELL_SIZE

class Astar:
    def __init__(self):
        pass

    def heuristic(self, pos1, pos2):
        """
        Heuristic used to give priority for cells in astar search
        Args:
        pos1 ((int, int)): tuple (x, y)
        pos2 ((int, int)): tuple (x, y)
        """
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def search(self, cells, start, end):
        """
        Implements A* pathfinding algo
        Args:
        cells (class cells)
        start (tuple(int,int)):
        end (tuple(int,int)):

        """
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == end:
                break
            for next in cells.get_neighbours(current):
                next_value = cells.cell_value(next[0], next[1])
                if next_value != 0:
                    break
                new_cost = cost_so_far[current] + 1 
                if (next[0], next[1]) not in cost_so_far or new_cost < cost_so_far[(next[0], next[1])]:
                    cost_so_far[(next[0], next[1])] = new_cost
                    priority = new_cost + self.heuristic((next[0], next[1]), end)
                    frontier.put((next[0], next[1]), priority)
                    came_from[(next[0], next[1])] = current

        return came_from, cost_so_far
