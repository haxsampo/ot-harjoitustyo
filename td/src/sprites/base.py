import pygame
from services.load_image import load_image

class Base(pygame.sprite.Sprite):
    """
    The aim of the enemies
    """
    def __init__(self, pos_x, pos_y, size_x, size_y, img_name):
        super().__init__()
        self.image = load_image(img_name)
        self.image.set_colorkey((255, 255, 255))
        self.surf = pygame.Surface((size_x, size_y))
        self.surf.blit(self.image, (pos_x, pos_y))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self, level):
        """
        called from level.update()
        """
        blocks_hit_list = pygame.sprite.spritecollide(self, level.enemies, False)
        for enemy in level.enemies:
            col = pygame.sprite.collide_rect(self, enemy)
            if col:
                level.set_lives(level.get_lives()-1)
                enemy.kill()
