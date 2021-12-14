import unittest
import pygame

from sprites.enemy import Enemy
from sprites.tower import Tower
from level import Level
from cells import Cells
from wave import Wave
from global_values import *


class TestEnemy(unittest.TestCase):
    '''
    Args:
    '''
    def setUp(self):
        self.testEnemy = Enemy(50, 500, "gandalf.png", 1)
        #tee cells ja wave + life(int) ja syötä levelille
        cells = Cells(SCREEN_HEIGHT, SCREEN_WIDTH, CELL_SIZE)
        wave = Wave(1, 10, 2000, 50, 300)
        self.level = Level(wave, cells, 10)
        self.level.enemies.add(self.testEnemy)
        self.tower = Tower(100, 500, "tower.png", 50, 50, 250, 1000, self.level)
        self.level.towers.add(self.tower)

    def test_tower_blocks_movement(self):
        '''
        Tests whether enemies can walk into towers
        '''
        initial_coll = self.testEnemy.rect.colliderect(self.tower.rect)
        self.assertEqual(initial_coll, False)
        self.testEnemy.update(self.level.towers)
        post_move_coll = pygame.sprite.collide_rect(self.testEnemy, self.tower)
        self.assertEqual(post_move_coll, False)
