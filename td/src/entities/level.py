import pygame
from global_values import SCREEN_WIDTH, SCREEN_HEIGHT
from sprites.button import Button
from sprites.base import Base
from sprites.highlight import Highlight

class Level:
    """
    Holds gameobjects of a specific level, calls their update function
    Args:
    cells (list of lists): 0 = empty, 1 = tower/blocked
    lives (int): amount of lives player has for the level
    """

    def __init__(self, wave, cells, lives, pf_algo, pathfinder, score):
        self.score = score
        self.end = (SCREEN_WIDTH - 100, SCREEN_HEIGHT/2)
        self.start = (50, 300)
        self.pathfinder = pathfinder
        self.pf_algo = pf_algo
        self.cells = cells
        self.wave = wave
        self.environment = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.towers = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.highlights = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.lives = lives
        self.path = self.pathfinder.calc_path(self.start, self.end)
        self.two_sec_timer = 0

    def level_initialization(self, butt_funcs):
        """
        Gives level buttons, base etc
        Called in index
        args:
        butt_funcs (class ButtonFunctionHolder)
        """
        butt = Button(10, 530, "tykki_nappi.png", 70, 70, butt_funcs.flip_one)
        self.buttons.add(butt)
        base = Base(SCREEN_WIDTH - 100, SCREEN_HEIGHT/2, 96, 51, "base96x51.png")
        self.environment.add(base)
        highlight = Highlight(1, 1)
        self.highlights.add(highlight)

    def update(self, current_time):
        """
        Args:
            current_time (int): milliseconds since pygame.init() was called
        """
        self.environment.update(self)
        self.enemies.update()
        self.towers.update(self.enemies, current_time)
        self.projectiles.update()
        self.wave.update(current_time, self)
        self.highlights.update()
        self.timed_updates(current_time)

    def timed_updates(self, current_time):
        """
        Call timed, repeating updates here
            that should not fire every frame
        """
        self.two_sec_timer += current_time
        if self.two_sec_timer >= 2000:
            self.two_sec_timer = 0
            self.cells.reconfirm_cell_values_per_sprite(self.towers)

    def initialize_sprites(self):
        """
        Args:
        """
        self.all_sprites.add(self.projectiles)
        self.all_sprites.add(self.enemies)
        self.all_sprites.add(self.towers)
        self.all_sprites.add(self.environment)
        self.all_sprites.add(self.buttons)

    def towers_shoot(self):
        """
        Args:
        """
        for tower in self.towers:
            tower.check_for_enemies(self.enemies)

    def set_lives(self, value):
        """
        value (int): set lives to value
        """
        self.lives = value

    def get_lives(self):
        """
        Args:
        """
        return self.lives
