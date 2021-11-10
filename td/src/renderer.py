import pygame


class Renderer:
    def __init__(self, display):
        self._display = display

    def render(self):
        self._all_sprites.draw(self._display)

        pygame.display.update()