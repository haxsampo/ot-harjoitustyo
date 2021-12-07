import pygame

from pygame.locals import (# pylint: disable=no-name-in-module
    K_UP, # pylint: disable=unused-import
    K_DOWN, # pylint: disable=unused-import
    K_LEFT, # pylint: disable=unused-import 
    K_RIGHT, # pylint: disable=unused-import
    K_ESCAPE, # pylint: disable=unused-import
    KEYDOWN, # pylint: disable=unused-import
    QUIT, # pylint: disable=unused-import
    MOUSEBUTTONDOWN,
    K_1
)

class UserInput:
    '''
    Handles user input, remembers what keys have been pressed etc
    '''

    def __init__(self):
        self.one_active = 0

    def key_handler(self, event_key, game_loop):
        '''
        Args:
        event_key (pygame.key): pressed key
        game_loop (GameLoop): current running gameloop class
        '''
        if event_key == K_ESCAPE:
            game_loop.running = False

        if event_key == K_1:
            if self.one_active == 1:
                self.one_active = 0
            else:
                self.one_active = 1

    def flip_one(self):
        '''
        flips the value of one_active
        '''
        self.one_active ^= 1
        print("one flipped")
  
    def mouse_button_check(self, event_x, event_y, buttons):
        for button in buttons:
            if button.rect.collidepoint(event_x, event_y):
                button.run_func()
                return 1
