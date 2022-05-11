class Settings():
    """Class to hold game settings for object access"""
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Catcher settings
        self.catcher_speed = 4.0
        self.catcher_width = 120
        self.catcher_height = 200
        self.catcher_filename = "catcher.bmp"


        # Ball settings
        self.ball_speed = 2.0
        self.ball_width = 60
        self.ball_height = 60
        self.ball_filename = "ball.bmp"
        # Number of balls falling at a time
        self.num_balls = 1
