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
    K_p
)


class GameLoop:
    '''
    Not-Empty
    '''
    def __init__(self, clock, renderer, level, user_input):
        self._clock = clock
        self.running = False
        self._renderer = renderer
        self._level = level
        self._user_input = user_input

    def start(self):
        '''
        Args:
        '''
        self.running = True
        while True:
            self._handle_events()
            if self._user_input.pause == 0:
                self._renderer.render(self._user_input)
                current_time = self._clock.get_ticks()
                self._clock.tick(60)
                self._level.update(current_time)

    def _handle_events(self):
        '''
        Args:
        '''
        for event in pygame.event.get():
            if self._user_input.pause == 1:
                if event.type == KEYDOWN:
                    self._user_input.key_handler(event.key, self)
                elif event.type == QUIT:
                    self.running = False
            else:
                if event.type == KEYDOWN:
                    self._user_input.key_handler(event.key, self)
                elif event.type == MOUSEBUTTONDOWN:
                    event_x, event_y = event.pos
                    self.handle_mouse(event_x, event_y)
                elif event.type == QUIT:
                    self.running = False

        if not self.running:
            pygame.quit() # pylint: disable=no-member
            exit()


    #pura esim seuraaviin: rakennustsek, rakenna torni
    def handle_mouse(self, event_x, event_y):
        '''
        Args:
        '''
        print("event pos:", event_x, event_y)
        button_coll = self._user_input.mouse_button_check(event_x, event_y, self._level.buttons)
        if button_coll:
            return

        twr_x = int(event_x - (event_x % 5))
        twr_y = int(event_y - (event_y % 5))

        tmp_rect = pygame.Rect(1000, 1000, 50, 50)

        twr_in_bounds = self._level.cells.tower_in_bounds(event_x, event_y, tmp_rect)
        if twr_in_bounds:
            twr_fits = self._level.cells.tower_fits(event_x, event_y, tmp_rect)
            if twr_fits:
                self._level.cells.change_cells_to(event_x, event_y, tmp_rect, 1)
                tower = Tower(twr_x, twr_y, "tower.png", 5, 5, 250, 1000, self._level)
                self._level.towers.add(tower)
                self._level._initialize_sprites()
            else:
                print("tower doesn't fit :(")
        else:
            print("tower not in bounds :|")
        tmp_rect = None

        