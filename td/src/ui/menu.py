import pygame
import pygame_textinput
from sprites.button import Button

class Menu:
    """
    Args:
    """
    def __init__(self, highscore, repo):
        self.buttons = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.highscore = highscore
        self.repo = repo
        self.manager = pygame_textinput.TextInputManager(
            validator=lambda input: len(input) <= 15 and (input.isalpha() or len(input) == 0))
        self.text_input = pygame_textinput.TextInputVisualizer(manager=self.manager)
        self.player_name = ""

    def _initialize_sprites(self):
        self.all_sprites.add(self.buttons)

    def menu_initialization(self, butt_funcs):
        """
        Creates buttons for the main menu
        Args:
        butt_funcs (class ButtonFunctionHolder)
        """
        start_butt = Button(30, 20, "menu_start.png", 327, 90, butt_funcs.change_scene, "level")
        exit_butt = Button(30, 120, "main_menu_exit.png", 327, 90, butt_funcs.exit, False)
        self.buttons.add(start_butt)
        self.buttons.add(exit_butt)
        self._initialize_sprites()

    def menu_render(self, display):
        """
        Rendering of menu items
        """
        self.highscore.score_render(display)
        display.blit(self.text_input.surface, (30, 550))
        self.all_sprites.draw(display)
