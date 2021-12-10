import pygame

from sprites.tower import Tower

from pygame.locals import (# pylint: disable=no-name-in-module
    K_UP, # pylint: disable=unused-import
    K_DOWN, # pylint: disable=unused-import
    K_LEFT, # pylint: disable=unused-import 
    K_RIGHT, # pylint: disable=unused-import
    K_ESCAPE, # pylint: disable=unused-import
    KEYDOWN, # pylint: disable=unused-import
    QUIT, # pylint: disable=unused-import
    MOUSEBUTTONDOWN,
    K_1,
    K_p,
    K_g
)

class UserInput:
    '''
    Handles user input, remembers what keys have been pressed etc
    '''

    def __init__(self):
        self.one_active = 0
        self.pause = 0

    def key_handler(self, event_key, game_loop):
        '''
        Args:
        event_key (pygame.key): pressed key
        game_loop (GameLoop): current running gameloop class
        '''
        if event_key == K_ESCAPE:
            game_loop.running = False

        if event_key == K_p:
            self.pause ^= 1
            game_loop._notification.change_label("paused", (30, 30, 32))
            return

        if event_key == K_1:
            self.one_active ^= 1

        if event_key == K_g:
            game_loop._level.set_lives(0)
            #self.pause = 1
            #return({"game over":1})

        return None

    def flip_one(self):
        '''
        flips the value of one_active
        '''
        self.one_active ^= 1

    def mouse_button_check(self, event_x, event_y, buttons):
        '''
        Args:
        '''
        for button in buttons:
            if button.rect.collidepoint(event_x, event_y):
                button.run_func()
                return 1


    #pura esim seuraaviin: rakennustsek, rakenna torni
    def handle_mouse(self, event_x, event_y, level):
        '''
        Args:
        '''
        print("event pos:", event_x, event_y)
        button_coll = self.mouse_button_check(event_x, event_y, level.buttons)
        if button_coll:
            return

        twr_x = int(event_x - (event_x % 5))
        twr_y = int(event_y - (event_y % 5))

        tmp_rect = pygame.Rect(1000, 1000, 50, 50)

        twr_in_bounds = level.cells.tower_in_bounds(event_x, event_y, tmp_rect)
        if twr_in_bounds:
            twr_fits = level.cells.tower_fits(event_x, event_y, tmp_rect)
            if twr_fits:
                level.cells.change_cells_to(event_x, event_y, tmp_rect, 1)
                tower = Tower(twr_x, twr_y, "tower.png", 5, 5, 250, 1000, level)
                level.towers.add(tower)
                level._initialize_sprites()
            else:
                print("tower doesn't fit :(")
        else:
            print("tower not in bounds :|")
        tmp_rect = None
