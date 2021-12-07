import pygame


class Renderer:
    '''
    Args:
    '''
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self, user_input):
        '''
        Args:
        '''
        self._display.fill((255, 205, 200))
        self._level.all_sprites.draw(self._display)
        self.conditional_renders(user_input)
        for tower in self._level.towers:
            tower.draw_range(self._display)
        pygame.display.update()

    def conditional_renders(self, user_input):
        '''
        Checks user input before rendering
        '''
        if user_input.one_active:
            self._level.highlights.draw(self._display)
