import pygame
from gameloop import GameLoop
from clock import Clock
from renderer import Renderer
from enemy import Enemy


pygame.init()

def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255, 205, 200))
    gandalf = Enemy(100,100)
    screen.blit(gandalf.surf, (100,100))
    pygame.display.flip()
    clock = Clock()
    renderer = Renderer(screen)
    #level = Level()
    game_loop = GameLoop(clock,renderer)
    game_loop.start()

if __name__ == "__main__":
    main()