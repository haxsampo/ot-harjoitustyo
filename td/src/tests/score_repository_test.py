import unittest
import pygame
import csv

from repositories.score_repository import ScoreRepository

class TestScoreRepository(unittest.TestCase):
    """
    Tests for ScoreRepository class
    """

    def setUp(self):
        self.score_rep = ScoreRepository("tests/score_test.csv")
        self.csv_population()

    def tearDown(self):
        pass
        #poista csv
    
    def csv_population(self):
        """
        Populates the test csv with data
        """
        dada = [("vihdin kuningas", 100),
                ("kaino-vieno", 99),
                ("aku-ankka", 98)
                ]
        with open(self.score_rep._file_path, "w") as file:
            writer = csv.writer(file)