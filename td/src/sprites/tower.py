import pygame
import math
from load_image import load_image
from sprites.projectile import Projectile

#shoot_cd in ms


class Tower(pygame.sprite.Sprite):
    '''
    Args:
    '''
    def __init__(self, x, y, imgName, size_x, size_y, shoot_range, shoot_cd, level):
        super().__init__()
        self.image = load_image(imgName)
        self.image.set_colorkey((255, 255, 255))
        self.surf = pygame.Surface((size_x, size_y))
        # self.surf.blit(self.image,(x-(size_x/2),y-(size_y/2)))
        self.surf.blit(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.range = shoot_range
        self.last_shot_time = -10
        self.shoot_cd = shoot_cd
        self._level = level

    def update(self, enemies, current_time):
        '''
        Args:
        enemies (pygame.sprite.Group): enemy sprites in the level
        current_time (int): milliseconds since pygame.init() was called
        '''
        self.check_for_enemies(enemies, current_time)

    def draw_range(self, surf):
        '''
        Args:
        surf (pygame.Surface): wants the game background. 
        '''
        pygame.draw.circle(surf, (0, 0, 255),
                           (self.rect.x, self.rect.y), self.range, 2)

    def check_for_enemies(self, enemies, current_time):
        '''
        Args:
        enemies (pygame.sprite.Group): enemy sprites in the level
        current_time (int): milliseconds since pygame.init() was called
        '''
        for enemy in enemies:
            if math.hypot(self.rect.x - enemy.rect.x, self.rect.y - enemy.rect.y) < self.range:
                self.shoot(current_time, enemy)

    def shoot(self, current_time, enemy):
        '''
        Args:
        enemies (pygame.sprite.Group): enemy sprites in the level
        current_time (int): milliseconds since pygame.init() was called
        '''
        if current_time - self.last_shot_time > self.shoot_cd:
            print("paupau")
            self.last_shot_time = current_time
            new_pr = Projectile(self.rect.x, self.rect.y,
                                "projectile.png", 10, 10, enemy, 50, 1)
            self._level.projectiles.add(new_pr)
            self._level.all_sprites.add(self._level.projectiles)
