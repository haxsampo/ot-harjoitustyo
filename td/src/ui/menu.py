import pygame
from sprites.button import Button

class Menu:
    '''
    Args:
    '''
    def __init__(self):
        self.main_buttons = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def _initialize_sprites(self):
        self.all_sprites.add(self.main_buttons)

    def menu_initialization(self, user_input):
        '''
        Creates buttons for the main menu
        Args:
        menu (class Menu):
        user_input (class UserInput)
        '''
        start_butt = Button(30, 20, "main_menu_start.png", 327, 90, user_input.new_game)
        exit_butt = Button(30, 150, "main_menu_exit.png", 327, 90, user_input.exit)
        self.main_buttons.add(start_butt)
        self.main_buttons.add(exit_butt)
        self._initialize_sprites()

