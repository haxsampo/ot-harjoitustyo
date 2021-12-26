from sprites.enemy import Enemy
from global_values import ENEMY_SPAWN_LOCATION

class Wave:
    """
    Holds and releases enemies with given intervals
    """

    def __init__(self, enemies_per_spawn, enemies_per_wave, cooldown, pos_x, pos_y):
        """
        Args:
            cooldown (int): in ms; how often enemies spawn
            enemies_per_wave (int) 
        """
        self.enemies_per = enemies_per_spawn
        self.cooldown = cooldown
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.last_spawn = 0
        self.enemies_per_wave = enemies_per_wave
        self.enemies_spawned = 0

    def update(self, current_time, level):
        """
        Args:
            current_time (int): milliseconds since pygame.init() was called
        """
        if current_time - self.last_spawn > self.cooldown:
            self.last_spawn = current_time
            if self.enemies_per_wave >= self.enemies_spawned:
                gandalf = Enemy(ENEMY_SPAWN_LOCATION[0],
                                ENEMY_SPAWN_LOCATION[1],
                                "gandalf.png",
                                20, level.path)
                level.enemies.add(gandalf)
                level.initialize_sprites()
