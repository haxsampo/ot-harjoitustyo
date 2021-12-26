import unittest
import pygame
import csv
from repositories.score_repository import ScoreRepository
from config import SCORES_FILE

class TestScoreRepository(unittest.TestCase):
    """
    Tests for ScoreRepository class
    """

    def setUp(self):
        #self.score_rep = ScoreRepository("tests/score_test.csv")SCORES_FILE
        #self.csv_population()
        self.repo = ScoreRepository(SCORES_FILE)
        self.repo.delete_all()
        self.namescore1 = ("kalle", 100)
        self.namescore2 = ("pentti", 50)

    def test_new_score(self):
        """
        Slap in value, check if it gives the same back
        """
        self.repo.new_score(self.namescore1[0], self.namescore1[1])
        alls = self.repo.find_all()
        self.assertEqual(len(alls), 1)
        self.assertEqual(self.namescore1[1], alls[0][1])
