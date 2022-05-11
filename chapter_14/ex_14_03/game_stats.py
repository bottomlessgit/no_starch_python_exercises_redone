class GameStats():
    """Class to hold game level variables that chagne during gameplay"""
    def __init__(self, settings):
        """Initializes GameStats object"""
        self.misses_allowed = settings.misses_allowed
        self.reinitialize_stats()
        self.game_active = False


    def reinitialize_stats(self):
        """Initializes game stats for new game"""
        self.game_active = True
        self.misses_left = self.misses_allowed
