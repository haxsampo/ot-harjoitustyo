import pygame
from gameloop import GameLoop
from clock import Clock
from renderer import Renderer
from sprites.enemy import Enemy
#from sprites.projectile import Projectile
from sprites.tower import Tower
from wave import Wave
from level import Level
from sprites.highlight import Highlight

pygame.init() # pylint: disable=no-member


def main():
    ALFA = (255,255,255)
    #opp_unit_size = 50
    SCREEN_WIDTH = 800 #KOSKA PYTHON ON KAKKAPÄÄ, NIIN NÄÄ ON TALLENNETTU MYÖS LEVELIIN, VAIHDA KAIKKI KERRALLA
    SCREEN_HEIGHT = 600
    CELL_SIZE = 5
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #cells = list(range(0,int(SCREEN_HEIGHT/CELL_SIZE), 1))
    cells = [0]* int(SCREEN_HEIGHT/CELL_SIZE)
    for i in range(0,len(cells),1):
        x_list = [0] * int(SCREEN_WIDTH/CELL_SIZE)
        cells[i] = x_list

    pygame.display.flip()
    clock = Clock()
    wave = Wave(1, 10, 2000, 50, 300)
    level = Level(wave, cells)
    highlight = Highlight(1, 1)
    level.highlights.add(highlight)

    gandalf = Enemy(50, 300, "gandalf.png", 2)
    tower = Tower(500, 500, "tower.png", 15, 15, 250, 1000, level)

    gandalf2 = Enemy(50, 500, "gandalf.png", 2)
    tower2 = Tower(100, 500, "tower.png", 50, 50, 250, 1000, level)
    level.enemies.add(gandalf)
    level.towers.add(tower)
    level.enemies.add(gandalf2)
    level.towers.add(tower2)
    #projectile = Projectile(450,450,"projectile.png",10,10,gandalf, opp_unit_size,1)
    # level.projectiles.add(projectile)

    level._initialize_sprites() # pylint: disable=protected-access
    renderer = Renderer(screen, level)
    game_loop = GameLoop(clock, renderer, level)
    game_loop.start()


if __name__ == "__main__":
    main()
