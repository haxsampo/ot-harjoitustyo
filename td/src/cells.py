import pygame
from pf.cell import Cell

class Cells:
    '''
    Args:
    '''

    def __init__(self, SCREEN_HEIGHT, SCREEN_WIDTH, CELL_SIZE, initial_value):
        self.a = 1
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.CELL_SIZE = CELL_SIZE
        self.cells = [0]* int(SCREEN_HEIGHT/CELL_SIZE)
        for i in range(0, len(self.cells), 1):
            x_list = [initial_value] * int(SCREEN_WIDTH/CELL_SIZE)
            self.cells[i] = x_list

        self.celler = [0]* int(SCREEN_HEIGHT/CELL_SIZE)
        for i in range(0,len(self.cells),1):
            x_list = [initial_value] * int(SCREEN_WIDTH/CELL_SIZE)
            for j in range(0,len(x_list),1):
                x_list[j] = Cell(j,i,0)
            self.celler[i] = x_list


    def cell_value(self, x_pos, y_pos):
        '''
        Args:
        x_pos (int): pixel width
        y_pos (int): pixel height
        return (int): the value of the cell in question
        0 = empty, 1 = tower/blocked
        '''
        if x_pos < 0 or y_pos < 0:
            return 1
        if x_pos > self.SCREEN_WIDTH or y_pos > self.SCREEN_HEIGHT:
            return 1

        x_cellified = int((x_pos - (x_pos % self.CELL_SIZE))/self.CELL_SIZE)
        y_cellified = int((y_pos - (y_pos % self.CELL_SIZE))/self.CELL_SIZE)
        ret_val = self.cells[y_cellified][x_cellified]
        return ret_val
    
    def cell_value_in_cells(self, x_pos, y_pos):
        '''
        Args:
        x_pos (int): n:th cell in width
        y_pos (int): m:th cell in height
        return (int): the value of the cell in question
        0 = empty, 1 = tower/blocked
        '''
        return self.cells[y_pos][x_pos]

    def tower_fits(self, x_pos, y_pos, tower_rect):
        '''
        Assumes that towers are rectangular
        Args:
        x_pos (int): position x of mouse click
        y_pos (int): position y of mouse click
        tower_rect (pygame.Rect): 
        Returns true if it fits, False if it doesn't
        '''
        x_cellified = int((x_pos - (x_pos % 5))/5)
        y_cellified = int((y_pos - (y_pos % 5))/5)
        #main_cell = self.cells[y_cellified][x_cellified]
        #10*10 alueelta kaikki hmm miten
        tower_cell_width = int(tower_rect.width / self.CELL_SIZE)
        tower_cell_height = int(tower_rect.height / self.CELL_SIZE)
        ret_val = True
        for y in range(y_cellified, y_cellified+tower_cell_height):
            for x in range(x_cellified, x_cellified+tower_cell_width):
                cell_value = self.cells[y][x]
                if cell_value != 0:
                    ret_val = False

        return ret_val

    def change_cells_to(self, x_pos, y_pos, rect_area, value):
        '''
        Args:
        x_pos, y_pos (int): click values, starting cell calculated from these
        rect_area (pygame.Rect): what area do we want to cover to be changed
        value (int): what value the cells should be after the change
        '''
        x_cellified = int((x_pos - (x_pos % 5))/5)
        y_cellified = int((y_pos - (y_pos % 5))/5)
        tower_cell_width = int(rect_area.width / self.CELL_SIZE)
        tower_cell_height = int(rect_area.height / self.CELL_SIZE)
        for y in range(y_cellified, y_cellified+tower_cell_height):
            for x in range(x_cellified, x_cellified+tower_cell_width):
                self.cells[y][x] = value

    def tower_in_bounds(self, event_x, event_y, rect):
        '''
        Args:
        event_x (int):
        event_y (int):
        rect (pygame.Rect):
        '''
        twr_x = int(event_x - (event_x % 5))
        twr_y = int(event_y - (event_y % 5))
        if rect.width + twr_x > self.SCREEN_WIDTH:
            return False
        if rect.height + twr_y > self.SCREEN_HEIGHT:
            return False
        return True

    def get_neighbours(self, location):
        '''
        Args:
        location ((int,int), tuple): in cells

        Return:
        list of class Cell
        '''
        left = Cell(location[0]-1, location[1], self.cells[location[1]][location[0]-1])
        up = Cell(location[0], location[1]-1, self.cells[location[1]-1][location[0]])
        right = Cell(location[0]+1, location[1], self.cells[location[1]][location[0]+1])
        down = Cell(location[0], location[1]+1, self.cells[location[1]+1][location[0]])
        return [left, right, up, down]