import pygame


class Renderer:
    '''
    Args:
    '''
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self):
        '''
        Args:
        '''
        self._display.fill((255, 205, 200))
        self._level.all_sprites.draw(self._display)
        for tower in self._level.towers:
            tower.draw_range(self._display)
        pygame.display.update()
