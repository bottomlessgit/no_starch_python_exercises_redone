class Settings():
    """Class that holds all game settings"""
    def __init__(self):
        # Screen settings
        self.screen_dimensions = (self.screen_width, self.screen_height) = 1200, 800
        self.bg_color = (0, 0, 0)
        # Ship settings
        self.ship_filename = "ship.bmp"
        self.ship_dimensions = (self.ship_width, self.ship_height) = 60, 100
        self.ship_speed = 3.0
        self.lives = 3 # Number of lives lost before game over
        # Bullet settings
        self.bullet_color = (100, 10, 10)
        self.bullet_dimensions = (self.bullet_width, self.bullet_height) = 4, 20
        self.bullet_speed = 3.5
        # Alien settings
        self.alien_filename = "alien.bmp"
        self.alien_dimensions = (self.alien_width, self.alien_height) = 30, 30
        self.alien_spacing_x = 30
        self.alien_spacing_y = 30
        self.alien_ship_start_dist = 400 # Initial y distance between fleet and bottom
        self.alien_speed_x = 4
        self.alien_speed_y = 20
        self.alien_edge_distance = 200 # Initial xdistance from fleet to screen edge
        # Standard Button settings
        self.button_dimensions = (200, 100)
        self.button_font_size = 80
        self.button_color = (180, 180, 140)
        self.button_text_color = (0, 0, 20)


        # Now calculate number of rows and columns of aliens for creating alien fleet
        available_space_x = self.screen_width - self.alien_edge_distance + self.alien_spacing_x
        self.num_aliens_in_row = available_space_x // (self.alien_spacing_x + self.alien_width)
        available_space_y = self.screen_height - self.alien_ship_start_dist + self.alien_spacing_y
        self.num_rows = available_space_y // (self.alien_spacing_y + self.alien_height)
