import math
import pygame
from services.load_image import load_image


class Projectile(pygame.sprite.Sprite):
    '''
    Args:
    '''
    def __init__(self, pos_x, pos_y, img_name, size_x, size_y, target, opp_unit_size, dmg):
        '''
        Args:
        pos_x (int): position on the screen
        pos_y (int): position on the screen
        img_name (string): image file name
        size_x (int): size of sprite
        size_y (int): size of sprite
        target (class enemy): towards which the projectile will move
        opp_unit_size (int): used to calculate what range from target counts as a hit
        dmg (int): how much dmg this projectile does
        '''
        super().__init__()
        self.image = load_image(img_name)
        self.speed = 2
        self.surf = pygame.Surface((size_x, size_y))
        self.surf.blit(self.image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.target = target
        self.dmg = dmg
        self.enemy_size = opp_unit_size

    def update(self):
        '''
        Args:
        '''
        self.collision_detection()
        if self.target.rect.x > self.rect.x:
            self.rect.x += 1*self.speed
        else:
            self.rect.x -= 1*self.speed

        if self.target.rect.y > self.rect.y:
            self.rect.y += 1*self.speed
        else:
            self.rect.y -= 1*self.speed

    def collision_detection(self):
        '''
        doesn't actually check collision, but range to target
        Args:
        '''
        if math.hypot(self.rect.x - self.target.rect.x, self.rect.y - self.target.rect.y) < (self.enemy_size/2):
            self.target.take_damage(self.dmg)
            self.kill()
