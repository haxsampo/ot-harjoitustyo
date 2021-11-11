import pygame
from gameloop import GameLoop
from clock import Clock
from renderer import Renderer
from sprites.enemy import Enemy
from level import Level


pygame.init()

def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pygame.display.flip()
    clock = Clock()
    level = Level()
    gandalf = Enemy(100,100, "gandalf.png")
    level.enemies.add(gandalf)
    level._initialize_sprites()
    renderer = Renderer(screen,level)
    game_loop = GameLoop(clock,renderer,level)
    game_loop.start()

if __name__ == "__main__":
    main()