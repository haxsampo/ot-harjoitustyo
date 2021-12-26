import unittest
import pygame
from sprites.enemy import Enemy
from sprites.projectile import Projectile

class TestProjectile(unittest.TestCase):

    def test_collision_detection(self):
        """
        and update
        """
        test_enemy = Enemy(25, 25, "gandalf.png", 1, [(0, 0)])
        projs = pygame.sprite.Group()
        proj = Projectile(20, 20,
                          "projectile.png", 10, 10, test_enemy, 50, 1)
        projs.add(proj)
        self.assertEqual(len(projs), 1)
        proj.update()
        self.assertEqual(len(projs), 0)
