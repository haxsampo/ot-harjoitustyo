import pygame
from load_image import load_image

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self._image = load_image("gandalf.png")
        self.surf = pygame.Surface((50,50))
        self.surf.blit(self._image,(0,0))
        self.rect = self._image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        a = 1