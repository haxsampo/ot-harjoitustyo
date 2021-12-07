import pygame
from load_image import load_image

class Button(pygame.sprite.Sprite):
    '''
    Nabbi
    '''
    def __init__(self, pos_x, pos_y, img_name, size_x, size_y, button_func):
        super().__init__()
        self.image = load_image(img_name)
        self.image.set_colorkey((255, 255, 255))
        self.surf = pygame.Surface((size_x, size_y))
        self.surf.blit(self.image, (pos_x, pos_y))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.func = button_func
        print(self.func)
        self.func()

    def run_func(self):
        '''
        Runs the function given in init
        '''
        self.func()
