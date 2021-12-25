import unittest
import pygame

from sprites.enemy import Enemy
from sprites.tower import Tower
from level import Level
from cells import Cells
from wave import Wave
from global_values import POINTS_PER_FRAME, ENEMY_KILL_SCORE
from pf.astar import Astar
from pf.pathfinding import Pathfind
from score_keeper import ScoreKeeper


class TestEnemy(unittest.TestCase):
    """
    Args:
    """
    def setUp(self):
        self.testEnemy = Enemy(50, 500, "gandalf.png", 1, [(0,0)])
        #tee cells ja wave + life(int) ja syötä levelille
        cells = Cells(0)
        wave = Wave(1, 10, 2000, 50, 300)
        astar = Astar(cells)
        pf = Pathfind(cells, astar)
        score = ScoreKeeper(ENEMY_KILL_SCORE, POINTS_PER_FRAME)
        self.level = Level(wave, cells, 10, astar, pf, score)
        self.level.enemies.add(self.testEnemy)
        self.tower = Tower(100, 500, "tower.png", 50, 50, 250, 1000, self.level)
        self.level.towers.add(self.tower)

    def test_tower_blocks_movement(self):
        """
        Tests whether enemies can walk into towers
        """
        initial_coll = self.testEnemy.rect.colliderect(self.tower.rect)
        self.assertEqual(initial_coll, False)
        self.testEnemy.update()
        post_move_coll = pygame.sprite.collide_rect(self.testEnemy, self.tower)
        self.assertEqual(post_move_coll, False)
