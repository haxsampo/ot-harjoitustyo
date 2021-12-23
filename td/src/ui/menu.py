import pygame
import pygame_textinput
from sprites.button import Button

class Menu:
    """
    Args:
    """
    def __init__(self, highscore):
        self.buttons = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.highscore = highscore
        self.txt_input = pygame_textinput.TextInputVisualizer()
        self.player_name = ""

    def _initialize_sprites(self):
        self.all_sprites.add(self.buttons)

    def menu_initialization(self, butt_funcs):
        """
        Creates buttons for the main menu
        Args:
        menu (class Menu):
        user_input (class UserInput)
        """
        start_butt = Button(30, 20, "menu_start.png", 327, 90, butt_funcs.change_scene, "level")
        #score_butt = Button(30, 180, "highscore.png", 327, 90, butt_funcs.change_scene, "scores")
        exit_butt = Button(30, 120, "main_menu_exit.png", 327, 90, butt_funcs.exit, False)
        self.buttons.add(start_butt)
        #self.main_buttons.add(score_butt)
        self.buttons.add(exit_butt)
        self._initialize_sprites()

    def menu_render(self, display):
        """
        Rendering of menu items
        """
        self.highscore.score_render(display)
        display.blit(self.txt_input.surface, (30, 450))
        self.all_sprites.draw(display)
