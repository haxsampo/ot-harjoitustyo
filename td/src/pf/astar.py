from pf.priorityqueue import PriorityQueue
from pf.cell import Cell
import collections

class Astar:
    def __init__(self, cells):
        self.cells = cells

    def heuristic(self, pos1, pos2):
        '''
        Args:
        pos1 ((int, int)): tuple (x, y)
        pos2 ((int, int)): tuple (x, y)
        '''
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def search(self, cells, start, end):
        '''
        Args:
        cells (class cells)
        start (tuple):
        end (tuple):

        '''
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
                if next.value != 0:
                    break
                new_cost = cost_so_far[current] + 1 # implement weighted graph costs here if required
                if (next.x, next.y) not in cost_so_far or new_cost < cost_so_far[(next.x, next.y)]:
                    cost_so_far[(next.x, next.y)] = new_cost
                    priority = new_cost + self.heuristic((next.x, next.y), end)
                    frontier.put((next.x, next.y), priority)
                    came_from[(next.x, next.y)] = current

        return came_from, cost_so_far
