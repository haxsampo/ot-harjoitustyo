import pygame
from load_image import load_image

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x, y, img_name, health):
        super().__init__()
        self.image = load_image(img_name)
        self.image.set_colorkey((255,255,255))
        self.surf = pygame.Surface((50,50))
        self.surf.blit(self.image,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health

    def update(self):
        self.check_health()
        self.rect.x = self.rect.x + 1
        #self.rect.y = self.rect.y + 1

    def check_health(self):
        if self.health <= 0:
            self.kill()
    
    def take_damage(self, dmg):
        self.health -= dmg