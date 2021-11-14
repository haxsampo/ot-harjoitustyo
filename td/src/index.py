import pygame
from gameloop import GameLoop
from clock import Clock
from renderer import Renderer
from sprites.enemy import Enemy
from sprites.projectile import Projectile
from sprites.tower import Tower
from level import Level

pygame.init()

def main():
    #alpha = (255,255,255)
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    OPP_UNIT_SIZE = 50
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pygame.display.flip()
    clock = Clock()
    level = Level()
    gandalf = Enemy(50,300, "gandalf.png", 2)
    tower = Tower(500,500,"tower.png", 50, 50, 250, 1000,level)
    level.enemies.add(gandalf)
    level.towers.add(tower)
    #projectile = Projectile(450,450,"projectile.png",10,10,gandalf, OPP_UNIT_SIZE,1)
    #level.projectiles.add(projectile)

    level._initialize_sprites()
    renderer = Renderer(screen,level)
    game_loop = GameLoop(clock,renderer,level)
    game_loop.start()

if __name__ == "__main__":
    main()