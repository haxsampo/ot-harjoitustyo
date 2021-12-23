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
from pf.astar import Astar
from global_values import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE
from pf.pathfinding import Pathfind
from score_keeper import ScoreKeeper
from ui.button_functions import ButtonFunctionHolder
from ui.highscore import Highscore
from config import SCORES_FILE
from repositories.score_repository import ScoreRepository

pygame.init() # pylint: disable=no-member

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screps = ScoreRepository(SCORES_FILE)
    cells = Cells(0)
    user_input = UserInput()
    butt_funcs = ButtonFunctionHolder(user_input)
    score = ScoreKeeper(10, 0.001)
    base = Base(SCREEN_WIDTH - 100, SCREEN_HEIGHT/2, 96, 51, "base96x51.png")
    #cells.change_cells_to(base.rect.x, base.rect.y, base.rect, 1)
    astar = Astar(cells)
    pygame.display.flip()
    clock = Clock()
    wave = Wave(1, 1, 2000, 50, 300)
    pathfinder = Pathfind(cells, astar)
    level = Level(wave, cells, 10, astar, pathfinder, score)
    highlight = Highlight(1, 1)
    level.highlights.add(highlight)
    level.environment.add(base)

    butt = Button(10, 530, "tykki_nappi.png", 70, 70, butt_funcs.flip_one)
    level.buttons.add(butt)
    notif = Notification(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    hiscore = Highscore(300, 400)
    menu = Menu(hiscore)
    menu.menu_initialization(butt_funcs)

    level._initialize_sprites() # pylint: disable=protected-access
    renderer = Renderer(screen, level, menu)
    game_loop = GameLoop(clock, renderer, level, user_input, notif, menu)
    game_loop.start()

if __name__ == "__main__":
    main()
