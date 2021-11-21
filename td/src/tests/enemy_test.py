import unittest
import pygame

from sprites.enemy import Enemy
from sprites.tower import Tower
from level import Level

class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.testEnemy = Enemy(50,500,"gandalf.png",1)
        self.level = Level()
        self.level.enemies.add(self.testEnemy)
        self.tower = Tower(100,500,"tower.png",50,50,250,1000)
        self.level.towers.add(self.tower)

    def test_tower_blocks_movement(self):
        initialColl = self.testEnemy.rect.colliderect(self.tower.rect)
        self.assertEqual(initialColl, False)
        self.testEnemy.update(self.level.towers)
        #postMoveColl = self.testEnemy.rect.colliderect(self.tower.rect)
        postMoveColl = pygame.sprite.collide_rect(self.testEnemy,self.tower)
        self.assertEqual(postMoveColl,False)
