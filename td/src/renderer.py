import pygame


class Renderer:
    '''
    Args:
    '''
    def __init__(self, display, level, menu):
        self._display = display
        self._level = level
        self._menu = menu

    def render(self, user_input, notifs, ground_rgb):
        '''
        Args:
        '''
        self._display.fill(ground_rgb)
        self._level.all_sprites.draw(self._display)
        self.conditional_renders(user_input, notifs)
        for tower in self._level.towers:
            tower.draw_range(self._display)
        pygame.display.update()

    def conditional_renders(self, user_input, notifs):
        '''
        Checks user input before rendering
        '''
        if user_input.pause == 1:
            notifs.display_notification()
        if self._level.lives == 0:
            notifs.display_notification()
        if user_input.one_active:
            self._level.highlights.draw(self._display)

    def main_menu_render(self, background_rgb):
        '''
        Args:
        background_rgb ((int, int, int))
        '''
        self._display.fill(background_rgb)
        self._menu.all_sprites.draw(self._display)
        pygame.display.update()
