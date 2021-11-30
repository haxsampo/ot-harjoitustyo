import pygame

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
