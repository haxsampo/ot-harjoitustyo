import pygame
from services.load_image import load_image

class Highlight(pygame.sprite.Sprite):
    '''
    Args:
    '''
    def __init__(self, x_pos, y_pos):
        '''
        Args:
        '''
        super().__init__()
        self.image = load_image("tower.png")
        self.image.set_alpha(100)
        self.image.set_colorkey((255, 255, 255))
        self.surf = pygame.Surface((5, 5))
        self.surf.blit(self.image, (x_pos, y_pos))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self):
        '''
        Args:
        '''
        pos = pygame.mouse.get_pos()
        mouse_y = pos[1]
        mouse_x = pos[0]
        self.rect.x = mouse_x - (mouse_x % 5)
        self.rect.y = mouse_y - (mouse_y % 5)
