

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
        self.ship_speed = 1.1
        self.ship_speedup_factor = 1.05
        # Target settings
        self.target_dimensions = (self.target_width, self.target_height) = (160, 160)
        self.target_color = (50, 80, 120)
        self.target_speed = 1.0
        self.target_speedup_factor = 1.1
        # Bullet settings
        self.bullet_dimensions = (16, 100)
        self.bullet_color = (200, 200, 200)
        self.bullet_speed = 5.5
        self.bullet_speedup_factor = 1.01
        #Button settings
        self.button_dimensions = (self.button_width, self.button_height) = (200, 120)
        self.button_font_size = 60
        self.button_color = (80, 0, 200)
        self.button_text_color = (200, 200, 0)
        self.start_button_text = "Start"

        # General stats settings
        self.misses_allowed = 10

    def speedup_bullets(self):
        """Speeds up bullets"""
        self.bullet_speed *= self.bullet_speedup_factor
        print(self.bullet_speed)


    def reinitialize_bullet_speed(self):
        """Sets bullet speed back to defualt"""
        self.bullet_speed = 5.5

