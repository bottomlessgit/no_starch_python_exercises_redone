class Settings():
    """Class to hold pertinent game settings"""

    def __init__(self):
        """Initializes game settings"""
        # Game window settings
        self.game_size = (1200, 800)
        self.bg_color = (0, 0, 0)

        # Rocket settings
        self.rocket_filename = "rocket.bmp"
        self.rocket_dimensions = (100, 100)
        self.rocket_horizontal_speed = 1.0
        self.rocket_vertical_speed = 1.5