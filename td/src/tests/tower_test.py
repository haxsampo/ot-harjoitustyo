import unittest
import pygame
from sprites.tower import Tower
from sprites.projectile import Projectile
from sprites.enemy import Enemy
from tower_values import tower1

class StubLevel:
    def __init__(self):
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.enemies)
        self.all_sprites.add(self.projectiles)

    def get_enemies(self):
        return self.enemies

class TestTower(unittest.TestCase):
    def setUp(self):
        level = StubLevel()
        self.twr = Tower((50, 50), "tower.png",
                         (tower1['size_x'],
                          tower1['size_x']),
                         tower1['shoot_range'],
                         tower1['shoot_cd'],
                         level)

    def test_update_shoot(self):
        enemy = Enemy(110, 110, "gandalf.png", 1, 0)
        self.twr._level.enemies.add(enemy)
        self.twr.update(self.twr._level.get_enemies(), 2000)
        self.assertEqual(len(self.twr._level.projectiles), 1)
