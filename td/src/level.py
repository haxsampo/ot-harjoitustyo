import pygame
#from sprites.enemy import Enemy
from load_image import load_image

CELL_SIZE = 5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Level:
    '''
    Args:
    cells (list of lists): 0 = empty, 1 = tower/blocked
    '''

    def __init__(self, wave, cells):
        self.cells = cells
        self.wave = wave
        self.enemies = pygame.sprite.Group()
        self.towers = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.highlights = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def update(self, current_time):
        '''
        Args:
            current_time (int): milliseconds since pygame.init() was called
        '''
        self.enemies.update(self.towers)
        self.towers.update(self.enemies, current_time)
        self.projectiles.update()
        self.wave.update(current_time, self)
        self.highlights.update()

    def _initialize_sprites(self):
        '''
        Args:
        '''
        self.all_sprites.add(self.projectiles)
        self.all_sprites.add(self.enemies)
        self.all_sprites.add(self.towers)
        self.all_sprites.add(self.highlights)

    def towers_shoot(self):
        '''
        Args:
        '''
        for tower in self.towers:
            tower.check_for_enemies(self.enemies)

    def cell_value(self, x_pos, y_pos):
        '''
        Args:
        return (int): the value of the cell in question
        0 = empty, 1 = tower/blocked
        '''
        x_cellified = int((x_pos - (x_pos % 5))/5)
        y_cellified = int((y_pos - (y_pos % 5))/5)
        ret_val = self.cells[y_cellified][x_cellified]
        return ret_val

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
        tower_cell_width = int(tower_rect.width / CELL_SIZE)
        tower_cell_height = int(tower_rect.height / CELL_SIZE)
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
        tower_cell_width = int(rect_area.width / CELL_SIZE)
        tower_cell_height = int(rect_area.height / CELL_SIZE)
        for y in range(y_cellified, y_cellified+tower_cell_height):
            for x in range(x_cellified, x_cellified+tower_cell_width):
                self.cells[y][x] = value


    #def build_tower(self, x_pos, y_pos):

    def tower_in_bounds(self, event_x, event_y, rect):
        twr_x = int(event_x - (event_x % 5))
        twr_y = int(event_y - (event_y % 5))
        if rect.width + twr_x > SCREEN_WIDTH:
            return False
        if rect.height + twr_y > SCREEN_HEIGHT:
            return False
        return True
        