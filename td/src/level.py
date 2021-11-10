import pygame
from enemy import Enemy


class Level:
    def __init__(self):
        self.enemies = pygame.sprite.Group()

    def update(self, current_time):
        self.enemies.update()