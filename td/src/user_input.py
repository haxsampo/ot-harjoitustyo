import pygame
from inspect import signature

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
        return None

    def mouse_button_check(self, event_x, event_y, buttons, game_loop):
        '''
        Args:
        buttons (pygame.sprite.SpriteGroup)
        '''
        ret = 0
        for button in buttons:
            if button.rect.collidepoint(event_x, event_y):
                sig = signature(button.func)
                if len(sig.parameters) >= 1:
                    button.run_func(game_loop)
                else:
                    button.run_func()
                ret = 1
        return ret

    #pura esim seuraaviin: rakennustsek, rakenna torni
    def handle_mouse(self, event_x, event_y, scene, level, game_loop=None):
        '''
        Args:
        event_x (int): pos x of click in pixels
        event_y (int): pos y of click event in pixels
        scene (string): menu/level
        level (class Menu or class Level):
        '''
        print("event pos:", event_x, event_y)
        if scene == "menu":
            self.mouse_button_check(event_x, event_y, level.main_buttons, game_loop)
            return
        if scene == "level":
            button_coll = self.mouse_button_check(event_x, event_y, level.buttons, game_loop)
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

    def new_game(self, args=None):
        '''
        starts a new game
        '''
        args.scene = "level"

    def exit(self, args=None):
        '''
        reh
        '''
        args.running = False

    def flip_one(self):
        '''
        flips the value of one_active
        '''
        self.one_active ^= 1
