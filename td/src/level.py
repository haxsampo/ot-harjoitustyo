import pygame
from sprites.enemy import Enemy


class Level:
    def __init__(self):
        self.enemies = pygame.sprite.Group()
        self.towers = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def update(self, current_time):
        self.enemies.update(self.towers)
        self.towers.update(self.enemies,current_time)
        self.projectiles.update()

    def _initialize_sprites(self):
        self.all_sprites.add(self.projectiles)
        self.all_sprites.add(self.enemies)
        self.all_sprites.add(self.towers)

    def towers_shoot(self):
        for tower in self.towers:
            tower.check_for_enemies(self.enemies)
