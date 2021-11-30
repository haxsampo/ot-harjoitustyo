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
)


class GameLoop:
    '''
    Not-Empty
    '''
    def __init__(self, clock, renderer, level):
        self._clock = clock
        self.running = False
        self._renderer = renderer
        self._level = level

    def start(self):
        '''
        Args:
        '''
        self.running = True
        while True:
            self._handle_events()
            self._renderer.render()
            current_time = self._clock.get_ticks()
            self._clock.tick(60)
            self._level.update(current_time)

    def _handle_events(self):
        '''
        Args:
        '''
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            elif event.type == QUIT:
                self.running = False

        if not self.running:
            pygame.quit() # pylint: disable=no-member
            exit()

    def mouse_test(self):
        pos = pygame.mouse.get_pos()
        y = pos[1]
        x = pos[0]
        x_round_down = x - (x % 5)
        y_round_down = y - (y % 5)
        tower = Tower(x_round_down, y_round_down, "tower.png", 5, 5, 250, 1000, self._level)
        self._level.towers.add(tower)
        #x_round_up = x + (5-(x % 5))
        #y_round_up = y + (5-(y % 5))
