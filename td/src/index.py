import pygame
from services.gameloop import GameLoop
from services.clock import Clock
from services.renderer import Renderer
from services.user_input import UserInput
from entities.wave import Wave
from entities.level import Level
from entities.cells import Cells
from entities.score_keeper import ScoreKeeper
from entities.menu import Menu
from sprites.button import Button
from sprites.base import Base
from sprites.highlight import Highlight
from global_values import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_KILL_SCORE, POINTS_PER_FRAME, LIVES
from pf.pathfinding import Pathfind
from pf.astar import Astar
from ui.button_functions import ButtonFunctionHolder
from ui.highscore import Highscore
from ui.notifications import Notification
from config import SCORES_FILE
from repositories.score_repository import ScoreRepository

pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    repo = ScoreRepository(SCORES_FILE)
    cells = Cells(0)
    user_input = UserInput()
    butt_funcs = ButtonFunctionHolder(user_input)
    score = ScoreKeeper(ENEMY_KILL_SCORE, POINTS_PER_FRAME)
    base = Base(SCREEN_WIDTH - 100, SCREEN_HEIGHT/2, 96, 51, "base96x51.png")
    astar = Astar()
    pygame.display.flip()
    clock = Clock()
    wave = Wave(1, 1, 2000, 50, 300)
    pathfinder = Pathfind(cells, astar)
    level = Level(wave, cells, LIVES, astar, pathfinder, score)
    highlight = Highlight(1, 1)
    level.highlights.add(highlight)
    level.environment.add(base)

    butt = Button(10, 530, "tykki_nappi.png", 70, 70, butt_funcs.flip_one)
    level.buttons.add(butt)
    notif = Notification(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    hiscore = Highscore(300, 400)
    menu = Menu(hiscore, repo)
    menu.menu_initialization(butt_funcs)

    level.initialize_sprites()
    renderer = Renderer(screen, level, menu)
    game_loop = GameLoop(clock, renderer, level, user_input, notif, menu, repo)
    game_loop.start()

if __name__ == "__main__":
    main()
