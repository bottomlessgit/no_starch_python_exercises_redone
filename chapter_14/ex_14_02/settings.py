

class Settings():
    """Class from which relevant game settings are accessed"""
    def __init__(self):
        """Initializes all game settings"""
        # Screen settings
        self.screen_dimensions = (self.screen_width, self.screen_height) = (1200, 800)
        self.screen_color = (0, 0, 0)
        # Ship settings
        self.ship_filename = "ship.bmp"
        self.ship_dimensions = (self.ship_width, self.ship_height) = (100, 60)
        self.ship_speed = 1.5
        # Target settings
        self.target_dimensions = (self.target_width, self.target_height) = (80, 120)
        self.target_color = (50, 80, 120)
        self.target_speed = 1.0
        # Bullet settings
        self.bullet_dimensions = (16, 4)
        self.bullet_color = (200, 200, 200)
        self.bullet_speed = 5.5
        #Button settings
        self.button_dimensions = (self.button_width, self.button_height) = (200, 120)
        self.button_font_size = 60
        self.button_color = (80, 0, 200)
        self.button_text_color = (200, 200, 0)
        self.start_button_text = "Start"

        # General stats settings
        self.misses_allowed = 3

