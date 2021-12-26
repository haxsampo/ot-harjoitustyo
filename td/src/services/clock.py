import pygame


class Clock:
    """
    Holds pygame.time.Clock and its functions
    """
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """
        Update the clock with framerate data, should be called once per frame
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """
        Returns time in ms
        """
        return pygame.time.get_ticks()
