import pygame
from load_image import load_image


class Enemy(pygame.sprite.Sprite):
    '''
    Enemy sprite
    '''
    def __init__(self, x, y, img_name, health):
        '''
        Args:
        x (int): position on the screen x
        y (int): position on the screen y
        img_name (string): name of the image file
        health (int): 
        '''
        super().__init__()
        self.image = load_image(img_name)
        self.image.set_colorkey((255, 255, 255))
        self.surf = pygame.Surface((50, 50))
        self.surf.blit(self.image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health

    def update(self, towers):
        '''
        Args:
        towers (pygame.sprite.group): all towers in level
        '''
        self.check_health()
        self.enemy_move(towers)

    def check_health(self):
        '''
        Args:
        '''
        if self.health <= 0:
            self.kill()

    def take_damage(self, dmg):
        '''
        Args:
        dmg (int): how much dmg should the enemy take
        '''
        self.health -= dmg

    def enemy_tower_collision(self, towers):
        '''
        Args:
        towers (pygame.sprite.group): all towers in level
        '''
        return pygame.sprite.spritecollide(self, towers, False)

    def enemy_move(self, towers):
        '''
        Args:
        '''
        #curX = self.rect.x
        #curY = self.rect.y
        self.rect.x += 1
        if not self.enemy_tower_collision(towers):
            return
        else:
            self.rect.y += 1
            self.rect.x -= 1
