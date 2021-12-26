import pygame

class Notification:
    """
    Displays text, like in game over screen
    """
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, display):
        self.pos_y = SCREEN_HEIGHT - 30
        self.pos_x = SCREEN_WIDTH / 2

        self.pont = pygame.font.SysFont(None, 65)
        self.label = self.pont.render("notif", True, (30, 200, 0))
        self._display = display

    def display_notification(self):
        """
        argless
        """
        #if user_input.pause == 1:
        self._display.blit(self.label, (100, 100))

    def change_label(self, txt, color=(33, 33, 33)):
        """
        Args:
        txt (string): text to be showed
        color ((int, int, int)): rgb value
        """
        self.label = self.pont.render(txt, True, color)
