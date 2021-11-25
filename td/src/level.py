import pygame
#from sprites.enemy import Enemy
from load_image import load_image


class Level:
    '''
    Args:
    '''
    def __init__(self):
        self.enemies = pygame.sprite.Group()
        self.towers = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def update(self, current_time):
        '''
        Args:
            current_time (int): milliseconds since pygame.init() was called
        '''
        self.enemies.update(self.towers)
        self.towers.update(self.enemies, current_time)
        self.projectiles.update()
        self.mouse_highlight()

    def _initialize_sprites(self):
        '''
        Args:
        '''
        self.all_sprites.add(self.projectiles)
        self.all_sprites.add(self.enemies)
        self.all_sprites.add(self.towers)

    def towers_shoot(self):
        '''
        Args:
        '''
        for tower in self.towers:
            tower.check_for_enemies(self.enemies)

    def mouse_highlight(self):
        '''
        Args:
        '''
        mpos = pygame.mouse.get_pos()
        hl_ = load_image("tower.png")
        hl_.set_colorkey((255, 255, 255))
        surf = pygame.Surface((50, 50))
        surf.blit(hl_, (mpos[0], mpos[1]))
        rect = hl_.get_rect()
        rect.x = mpos[0]
        rect.y = mpos[1]
        #blittaa backgroundiin