class GameStats():
    """Class to keep track of game statistics as game runs"""
    def __init__(self, settings):
        """Initializes gamesettings object"""
        self.settings = settings
        self.reset_stats()

    def reset_stats(self):
        """Initializes stats to default"""
        self.game_active = True
        self.balls_left = self.settings.missed_balls_permitted

    def ball_missed(self):
        """Changes game stats to reflect ball being missed"""
        self.balls_left -= 1
        if self.balls_left <= 0:
            self.game_active = False

