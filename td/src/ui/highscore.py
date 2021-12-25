"""
Handles displaying highscore on the mainscreen
"""
import pygame
from global_values import SCREEN_WIDTH

class Highscore:
    """
    Communicates with db_comms
    """
    def __init__(self, size_x, size_y):
        self.scores_list = ["jaska 100",
                            "kaapo 99",
                            "purjo-olavi 33"]
        self.surf = pygame.Surface((size_x, size_y))
        self.font = pygame.font.SysFont(None, 24)
        self.text = self.font.render('kakkapenis', True, (130, 0, 130))
        #self.textpos = self.text.get_rect(centerx=SCREEN_WIDTH/2+100, y=50)

    def score_render(self, display):
        """
        Called from renderer, displays the scores list
        Args:
        display (pygame.display): current renderer display
        """
        i = 1
        for score in self.scores_list:
            text = self.font.render(score, True, (130, 0, 130))
            textpos = self.text.get_rect(centerx=SCREEN_WIDTH/2+100, y=50+20*i)
            display.blit(text, textpos)
            i += 1

    def update_highscores(self, new_scores):
        """
        Replaces empty hiscore with a phrase
        """
        if not new_scores:
            self.scores_list = ["Once you play", "highscores will be", "displayed here"]
        else:
            self.scores_list = new_scores
