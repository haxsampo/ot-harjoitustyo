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
from sprites.base import Base
from ui.notifications import Notification
from ui.menu import Menu

pygame.init() # pylint: disable=no-member

def main():
    ALFA = (255, 255, 55)
    #opp_unit_size = 50
    SCREEN_WIDTH = 800 #KOSKA PYTHON ON KAKKAPÄÄ, NIIN NÄÄ ON TALLENNETTU MYÖS LEVELIIN, VAIHDA KAIKKI KERRALLA
    SCREEN_HEIGHT = 600
    CELL_SIZE = 5
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    cells = Cells(SCREEN_HEIGHT, SCREEN_WIDTH, CELL_SIZE)
    user_input = UserInput()

    base = Base(SCREEN_WIDTH - 100, SCREEN_HEIGHT/2, 96, 51, "base96x51.png")

    pygame.display.flip()
    clock = Clock()
    wave = Wave(1, 10, 2000, 50, 300)
    level = Level(wave, cells, 10)
    highlight = Highlight(1, 1)
    level.highlights.add(highlight)
    level.environment.add(base)
    #tower = Tower(500, 200, "tower.png", 15, 15, 250, 1000, level)
    #tower2 = Tower(100, 200, "tower.png", 50, 50, 250, 1000, level)
    #level.towers.add(tower)
    #level.towers.add(tower2)

    butt = Button(10, 530, "tykki_nappi.png", 70, 70, user_input.flip_one)
    level.buttons.add(butt)
    notif = Notification(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    menu = Menu()
    menu.menu_initialization(user_input)

    level._initialize_sprites() # pylint: disable=protected-access
    renderer = Renderer(screen, level, menu)
    game_loop = GameLoop(clock, renderer, level, user_input, notif, menu)
    game_loop.start()

if __name__ == "__main__":
    main()
