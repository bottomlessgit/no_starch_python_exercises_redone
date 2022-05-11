class Settings():
    """Class made to keep track of and access static and changing game settings"""
    # First static settings:
    # Screen settings
    def __init__(self):
        """Initialize settings object"""
        self.screen_dimensions = self.screen_width, self.screen_height = 1200, 800
        self.screen_color = (0, 0, 0)
        # Ship settings
        self.ship_filename = "ship.bmp"
        self.ship_dimensions = (self.ship_width, self.ship_height) = (60, 100)
        # Bullet settings
        self.bullet_dimensions = (self.bullet_width, self.bullet_height) = (200, 20)
        self.bullet_color = (150, 0, 0)
        # Alien settings
        self.alien_filename = "alien.bmp"
        self.alien_dimensions = (self.alien_width, self.alien_height) = (40, 40)
        # Alien fleet settings
        self.alien_spacing_x = 30
        self.alien_spacing_y = 30
        self.alien_start_space_x = 400 # Initial space between screen right and alien fleet
        self.alien_start_space_y = 400 # Initial space between screen bottom and alien fleet
        self.num_aliens_in_row = self.calculate_num_aliens_in_row()
        self.num_rows_in_fleet = self.calculate_num_rows_in_fleet()
        # Button settings
        self.button_dimensions = (self.button_width, self.button_height) = (300, 250)
        self.button_color = (120, 140, 120)
        self.button_text_color = (20, 0, 20)
        self.button_text_size = 60
        self.button_start_text = "START"
        # Scoreboard settings
        self.scoreboard_font_size = 40
        self.scoreboard_text_color = (100, 200, 100)
        self.life_emblem_dimensions = (self.life_emblem_width, self.life_emblem_height) = (30, 50)


        # General game settings
        self.lives = 3 # Number of lives
        # Fleet defeat settings changes
        self.ship_speed_increase_factor = 1.1
        self.bullet_speed_increase_factor = 1.05
        self.alien_x_speed_increase_factor = 1.05
        self.alien_y_speed_increase_factor = 1.05
        self.alien_points_increase_factor = 1.3



        # Now initialize default values for non-static settings
        self.set_default_settings()


    def calculate_num_aliens_in_row(self):
        """Function to calculate initial number of columns of aliens in fleet"""        
        alien_row_space = self.screen_width - self.alien_start_space_x + self.alien_spacing_x
        width_per_alien = self.alien_width + self.alien_spacing_x
        num_aliens_in_row = alien_row_space // width_per_alien
        return num_aliens_in_row


    def calculate_num_rows_in_fleet(self):
        """Function to calculate initial number of rows of aliens in fleet"""
        alien_col_space = self.screen_height - self.alien_start_space_y
        height_per_alien = self.alien_height + self.alien_spacing_y
        num_rows_in_fleet = alien_col_space // height_per_alien
        return num_rows_in_fleet



    # Now create a function to assign default values to changing settings
    def set_default_settings(self):
        """Initializes and reinitializes default values for settings that 
        change during gameplay"""
        # Ship settings
        self.ship_speed = 1.5
        # Bullet setting
        self.bullet_speed = 3.0
        # Alien settings
        self.alien_x_speed = .7
        self.alien_y_speed = 10.0
        self.alien_points = 1000


    def next_level(self):
        """Changes changing game settings in response to fleet defeat"""
        self.ship_speed *= self.ship_speed_increase_factor
        self.bullet_speed *= self.bullet_speed_increase_factor
        self.alien_x_speed *= self.alien_x_speed_increase_factor
        self.alien_y_speed *= self.alien_y_speed_increase_factor 
        self.alien_points = int(self.alien_points * self.alien_points_increase_factor)

