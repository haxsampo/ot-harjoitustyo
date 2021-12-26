import os
import pygame

dir = os.path.dirname(__file__)

def load_image(filename):
    """
    Helps with giving path to images
    """
    return pygame.image.load(
        os.path.join(dir, "assets", filename)
    )
