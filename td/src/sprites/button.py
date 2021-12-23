"""
Button UI element
Functions held in button_functions.py
"""
import pygame
from load_image import load_image

class Button(pygame.sprite.Sprite):
    """
    pos_x (int):
    pos_y (int):
    img_name (string):
    size_x (int):
    size_y (int):
    button_func (function): Clicking buttons fires the function given
    button_value (any): can be used to pass value or to change value to something when
        button_func is called
    """
    def __init__(self, pos_x, pos_y, img_name, size_x, size_y, button_func, button_value=None):
        super().__init__()
        self.image = load_image(img_name)
        self.image.set_colorkey((255, 255, 255))
        self.surf = pygame.Surface((size_x, size_y))
        self.surf.blit(self.image, (pos_x, pos_y))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.func = button_func
        self.button_value = button_value

    def run_func(self, *kwargs):
        '''
        Runs the function given in init
        '''
        self.func(*kwargs)
