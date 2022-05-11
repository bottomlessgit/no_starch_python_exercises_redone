class GameStats():
    """Class to hold stats and game-level info that changes thorughout gameplay"""
    def __init__(self, settings):
        """Initializes game stats object"""
        self.settings = settings
        self.reset_stats()


    def reset_stats(self):
        """Sets game stats to default for start of new game"""
        self.ships_left = self.settings.lives
        self.game_active = False


#    def handle_death(self):
#        """Responds to loss of ship life"""
#        self.ships_left -= 1
#        if self.ships_left == 0:
#            self.game_active = False
