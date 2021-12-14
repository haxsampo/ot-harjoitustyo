import pygame
from global_values import *

class GameLoop:
    '''
    Not-Empty
    '''
    def __init__(self, clock, renderer, level, user_input, notification, menu):
        self._clock = clock
        self.running = False
        self._renderer = renderer
        self._level = level
        self._user_input = user_input
        self.notification = notification
        self._menu = menu
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
            if not self.running:
                pygame.quit() # pylint: disable=no-member
                exit()

    def menu_scene(self):
        '''
        Args:
        '''
        self._menu_events()
        self._renderer.main_menu_render((20, 180, 190))

    def level_scene(self):
        '''
        Args:
        '''
        self._handle_events()
        if self._level.lives <= 0:
            self.level_over()
        self._renderer.render(self._user_input, self.notification, (255, 205, 200))
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
                    self._user_input.handle_mouse(event_x, event_y, self.scene, self._level, self)
                elif event.type == QUIT:
                    self.running = False

    def _menu_events(self):
        '''
        args:
        '''
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == MOUSEBUTTONDOWN:
                event_x, event_y = event.pos
                self._user_input.handle_mouse(event_x, event_y, self.scene, self._menu, self)

    def level_over(self):
        '''
        args:
        '''
        self._user_input.pause = 1
        self.notification.change_label("game over :(")

