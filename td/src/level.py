import pygame
from enemy import Enemy


class Level:
    def __init__(self):
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def update(self, current_time):
        self.enemies.update()

    def _initialize_sprites(self):
        self.all_sprites.add(self.enemies)