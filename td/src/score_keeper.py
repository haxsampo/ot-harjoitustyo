class ScoreKeeper:
    """
    Holds score during game session
    Args:
    dead_enemy_value (int): score per dead enemy
    survival_time_value (float): score per survived tick
    """

    def __init__(self, dead_enemy_value, survival_time_value):
        self.score = 0
        self.dead_enemy_value = dead_enemy_value
        self.level_start_time = 0
        self.survival_time_value = survival_time_value

    def level_start(self, ticks):
        """
        clock (class Clock)
        """
        self.level_start_time = ticks

    def killed_enemy(self):
        """
        """
        self.score += self.dead_enemy_value
    
    def survival_time_count(self, ticks):
        """
        Return:
        Current score + survival time score
        clock (class Clock)
        """
        time_score = (ticks - self.level_start_time) * self.survival_time_value
        return self.score + time_score
