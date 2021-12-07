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
        self.buttons = pygame.sprite.Group()

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
        #self.all_sprites.add(self.highlights)
        self.all_sprites.add(self.buttons)

    def towers_shoot(self):
        '''
        Args:
        '''
        for tower in self.towers:
            tower.check_for_enemies(self.enemies)

