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
from global_values import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_KILL_SCORE, POINTS_PER_FRAME, LIVES
from pf.pathfinding import Pathfind
from pf.astar import Astar
from ui.button_functions import ButtonFunctionHolder
from ui.highscore import Highscore
from ui.notifications import Notification
from config import SCORES_FILE
from repositories.score_repository import ScoreRepository

pygame.init() # pylint: disable=no-member

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    user_input = UserInput()
    butt_funcs = ButtonFunctionHolder(user_input)
    pygame.display.flip()
    
    cells = Cells(0)
    astar = Astar()
    pathfinder = Pathfind(cells, astar)
    wave = Wave(1, 1, 2000, 50, 300)
    score = ScoreKeeper(ENEMY_KILL_SCORE, POINTS_PER_FRAME)
    level = Level(wave, cells, LIVES, astar, pathfinder, score)
    level.level_initialization(butt_funcs)

    notif = Notification(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    hiscore = Highscore(300, 400)
    repo = ScoreRepository(SCORES_FILE)
    menu = Menu(hiscore, repo)
    menu.menu_initialization(butt_funcs)
    level.initialize_sprites()
    renderer = Renderer(screen, level, menu)
    clock = Clock()
    game_loop = GameLoop(clock, renderer, level, user_input, notif, menu, repo)
    game_loop.start()

if __name__ == "__main__":
    main()
