import pygame
import math
from load_image import load_image


class Enemy(pygame.sprite.Sprite):
    """
    Enemy class sprite
    """
    def __init__(self, pos_x, pos_y, img_name, health, path, speed=1):
        """
        Args:
        x (int): position on the screen x
        y (int): position on the screen y
        img_name (string): name of the image file
        health (int):
        """
        super().__init__()
        self.path = path
        self.path_index = 0
        self.image = load_image(img_name)
        self.image.set_colorkey((255, 255, 255))
        self.surf = pygame.Surface((50, 50))
        self.surf.blit(self.image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.health = health
        self.speed = speed

    def update(self, towers, level):
        """
        Args:
        towers (pygame.sprite.group): all towers in level
        """
        self.check_health()
        self.enemy_move(towers, level)

    def check_health(self):
        """
        Args:
        """
        if self.health <= 0:
            self.kill()

    def take_damage(self, dmg):
        """
        Args:
        dmg (int): how much dmg should the enemy take
        """
        self.health -= dmg

    def enemy_tower_collision(self, towers):
        """
        Args:
        towers (pygame.sprite.group): all towers in level
        """
        return pygame.sprite.spritecollide(self, towers, False)

    def enemy_move(self, towers, level):
        """
        Args:
        """
        #tsekkaa onko currenttiin etäisyyttä
            #jos ei niin päivitä current
        #move to current
        self.update_target_coords(level)
        self.move_towards(self.path[self.path_index])
        """ self.rect.x += 1
        if not self.enemy_tower_collision(towers):
            return
        else:
            self.rect.y += 1
            self.rect.x -= 1 """

    def update_target_coords(self, level):
        """
        Checks whether enemy is close to the goal, and updates if closer than 0.5
        """
        #if path_index > len(path):
        #    self.path
        target_x = self.path[self.path_index][0]
        target_y = self.path[self.path_index][1]
        dif_x, dif_y = target_x - self.rect.x, target_y - self.rect.y
        dist = math.hypot(dif_x, dif_y)
        if dist < 0.5:
            self.path_index += 1

    def move_towards(self, target):
        """
        Calculates normalized vector towards target and moves towards it with self.speed
        Args:
        target ((int, int)): tuple, coordinates
        """
        dif_x, dif_y = target[0] - self.rect.x, target[1] - self.rect.y
        dist = math.hypot(dif_x, dif_y)
        dif_x, dif_y = dif_x / dist, dif_y / dist
        self.rect.x += dif_x * self.speed
        self.rect.y += dif_y * self.speed
