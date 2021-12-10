import pygame
#from sprites.tower import Tower

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


class GameLoop:
    '''
    Not-Empty
    '''
    def __init__(self, clock, renderer, level, user_input, notification):
        self._clock = clock
        self.running = False
        self._renderer = renderer
        self._level = level
        self._user_input = user_input
        self._notification = notification
        self.scene = "menu"

    def start(self):
        '''
        Args:
        '''
        self.running = True
        while True:
            if self.scene == "level":
                self.level_scene()
            elif self.scene == "menu":
                self.menu_scene()

    def menu_scene(self):
        self._handle_events()
        self._renderer.render(self._user_input, self._notification, (20, 180, 190))

    def level_scene(self):
        '''
        Args:
        '''
        self._handle_events()
        if self._level.lives <= 0:
            self.level_over()
        self._renderer.render(self._user_input, self._notification,(255, 205, 200))
        if self._user_input.pause == 0:
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
                    self._user_input.handle_mouse(event_x, event_y, self._level)
                elif event.type == QUIT:
                    self.running = False

        if not self.running:
            pygame.quit() # pylint: disable=no-member
            exit()

    def level_over(self):
        '''
        '''
        self._user_input.pause = 1
        self._notification.change_label("game over :(")