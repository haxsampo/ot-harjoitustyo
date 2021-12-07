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
from cells import Cells
from user_input import UserInput
from sprites.button import Button

pygame.init() # pylint: disable=no-member


def main():
    ALFA = (255, 255, 55)
    #opp_unit_size = 50
    SCREEN_WIDTH = 800 #KOSKA PYTHON ON KAKKAPÄÄ, NIIN NÄÄ ON TALLENNETTU MYÖS LEVELIIN, VAIHDA KAIKKI KERRALLA
    SCREEN_HEIGHT = 600
    CELL_SIZE = 5
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #cells = list(range(0,int(SCREEN_HEIGHT/CELL_SIZE), 1))
    """ cells = [0]* int(SCREEN_HEIGHT/CELL_SIZE)
    for i in range(0,len(cells),1):
        x_list = [0] * int(SCREEN_WIDTH/CELL_SIZE)
        cells[i] = x_list """
    cells = Cells(SCREEN_HEIGHT, SCREEN_WIDTH, CELL_SIZE)
    user_input = UserInput()

    pygame.display.flip()
    clock = Clock()
    wave = Wave(1, 10, 2000, 50, 300)
    level = Level(wave, cells)
    highlight = Highlight(1, 1)
    level.highlights.add(highlight)

    tower = Tower(500, 200, "tower.png", 15, 15, 250, 1000, level)
    tower2 = Tower(100, 200, "tower.png", 50, 50, 250, 1000, level)
    level.towers.add(tower)
    level.towers.add(tower2)

    butt = Button(10, 530, "tykki_nappi.png", 70, 70, user_input.flip_one)
    level.buttons.add(butt)

    level._initialize_sprites() # pylint: disable=protected-access
    renderer = Renderer(screen, level)
    game_loop = GameLoop(clock, renderer, level, user_input)
    game_loop.start()


if __name__ == "__main__":
    main()
