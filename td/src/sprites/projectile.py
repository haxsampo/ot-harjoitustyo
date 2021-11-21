import pygame
import math
from load_image import load_image

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img_name, size_x, size_y, target, OPP_UNIT_SIZE, dmg):
        super().__init__()
        self.image = load_image(img_name)
        self.speed = 2
        self.surf = pygame.Surface((size_x,size_y))
        self.surf.blit(self.image,(0,0))
        self.rect=self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.target = target
        self.dmg = dmg
        self.enemy_size = OPP_UNIT_SIZE

    def update(self):
        self.collision_detection()
        if self.target.rect.x > self.rect.x:
            self.rect.x += 1*self.speed
        else:
            self.rect.x -= 1*self.speed
        
        if self.target.rect.y > self.rect.y:
            self.rect.y += 1*self.speed
        else:
            self.rect.y -= 1*self.speed
    
    #doesn't actually check collision, but range to target
    def collision_detection(self):
        if math.hypot(self.rect.x - self.target.rect.x, self.rect.y - self.target.rect.y) < (self.enemy_size/2):
            self.target.take_damage(self.dmg)
            self.kill()


