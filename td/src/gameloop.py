import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class GameLoop:
    def __init__(self, clock, renderer):
        self._clock = clock
        self.running = False
        self._renderer = renderer

    def start(self):
        self.running = True
        while True:
            self._handle_events()
            #self._renderer.render()
            current_time = self._clock.get_ticks()
            self._clock.tick(60)
            #self._level.update(current_time)
            #self._render()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            elif event.type == QUIT:
                self.running = False

        if not self.running:
            pygame.quit()
            exit()


        