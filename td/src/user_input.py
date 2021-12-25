import pygame
from inspect import signature
from sprites.tower import Tower
from tower_values import tower1
from global_values import K_ESCAPE, K_p, K_1, K_g

class UserInput:
    """
    Handles user input, remembers what keys have been pressed etc
    Values are changed via butt_funcs and here
    """

    def __init__(self):
        self.one_active = 0
        self.pause = 0

    def key_handler(self, event_key, game_loop):
        """
        Args:
        event_key (pygame.key): pressed key
        game_loop (GameLoop): current running gameloop class
        """
        if event_key == K_ESCAPE:
            game_loop.running = False
        if event_key == K_p:
            self.pause ^= 1
            game_loop._notification.change_label("paused", (30, 30, 32))
            return
        if event_key == K_1:
            self.one_active ^= 1
        if event_key == K_g:
            game_loop._level.set_lives(0)

    def mouse_button_check(self, event_x, event_y, buttons, game_loop, scene_obj, scene_str):
        """
        Args:
        buttons (pygame.sprite.SpriteGroup)
        Returns:
        value 0 or 1 to tell handle_mouse whether event hit a button or not
        """
        ret = 0
        for button in buttons:
            if button.rect.collidepoint(event_x, event_y):
                button.run_func({'game_loop':game_loop,
                                 "button_value":button.button_value,
                                 'user_input':self,
                                 'scene_obj':scene_obj,
                                 'scene_str':scene_str})
                ret = 1
        return ret

    #pura esim seuraaviin: rakennustsek, rakenna torni
    def handle_mouse(self, event_x, event_y, scene_str, scene_obj, game_loop=None):
        """
        Checks mouse inputs for button events + tower building
        Args:
        event_x (int): pos x of click in pixels
        event_y (int): pos y of click event in pixels
        scene (string): menu/level
        level (class Menu or class Level):
        """
        print("event pos:", event_x, event_y)
        button_coll = self.mouse_button_check(event_x, event_y,
                                              scene_obj.buttons,
                                              game_loop, scene_obj, scene_str)
        if button_coll:
            return
        if self.one_active:
            self.build_tower(event_x, event_y, scene_obj)

    def build_tower(self, event_x, event_y, level):
        """
        Checks whether new tower fits in
        Builds a tower on given level, given coords
        Updates enemy paths
        Updates level level.path
        Args:
        """
        twr_x = int(event_x - (event_x % 5))
        twr_y = int(event_y - (event_y % 5))
        tmp_rect = pygame.Rect(event_x, event_y, tower1['size_x'], tower1['size_y'])
        twr_in_bounds = level.cells.tower_in_bounds(event_x, event_y, tmp_rect)
        if twr_in_bounds:
            twr_fits = level.cells.tower_fits(event_x, event_y, tmp_rect)
            spritegroups = [level.environment, level.enemies, level.buttons]
            sprites_overlap = self._spritegroup_overlap(tmp_rect, spritegroups)
            if twr_fits and not sprites_overlap:
                level.cells.change_cells_to(event_x, event_y, tmp_rect, 1)
                tower = Tower(twr_x, twr_y,
                              tower1['img_name'],
                              tower1['size_x'],
                              tower1['size_y'],
                              tower1['shoot_range'],
                              tower1['shoot_cd'],
                              level)
                level.towers.add(tower)
                level.initialize_sprites()
                level.pathfinder.update_paths(level.enemies, level.end)
                path_exists = level.pathfinder.calc_path(level.start, level.end)
                if path_exists:
                    level.path = path_exists
                else:
                    print("tower would block path")
            else:
                print("tower doesn't fit :(")
        else:
            print("tower not in bounds :|")
        tmp_rect = None

    def rect_overlap(self, rect, sprite_group):
        """
        Does given rectangle overlap any of the rects of given sprite group?
        Args:
        rect (pygame.Rect)
        sprite_group (pygame.sprite.Group)
        """
        overlap = False
        for sprite in sprite_group:
            if rect.colliderect(sprite.rect):
                overlap = True
        return overlap

    def _spritegroup_overlap(self, rect, list_of_spritegroups):
        for sprite_group in list_of_spritegroups:
            group_overlap = self.rect_overlap(rect, sprite_group)
            if group_overlap:
                return True
        return False