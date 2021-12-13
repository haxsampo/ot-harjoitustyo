import pygame

class Pathfind:
    '''
    Implents A* for enemy
    '''

    def __init__(self, cells):
        a=1
        self.cells = cells

    def calculate_path(self, start, end):
        a=2