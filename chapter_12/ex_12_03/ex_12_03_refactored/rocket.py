import pygame

class Rocket():
    """Class representing controllable rocket in game"""

    def __init__(self, settings, screen):
        """Initializes rocket attributes"""

        # Settings object for movement
        self.settings = settings

        # Get screen object to draw to
        self.screen = screen

        # Load rocket image
        self.image = pygame.image.load(settings.rocket_filename)

        # NOTE: The scale function hasn't been used in the textbook. The rocket img
        # was too large, so I use this function to scale it down to a smaller surface
        self.image = pygame.transform.scale(self.image, settings.rocket_dimensions)

        # get rect of screen for positioning
        self.screen_rect = self.screen.get_rect()

        # Get rect for changing rocket position
        self.rect = self.image.get_rect()

        # Initialize positoion
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Create precise x y position attributes for oprecise movement
        self.precise_center_x = float(self.rect.centerx)
        self.precise_center_y = float(self.rect.centery)


        # Flags to keep track of how rocket should move
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update Rocket position based on movement flags and position"""
        # Now handle movement
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.precise_center_x += self.settings.rocket_horizontal_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.precise_center_x -= self.settings.rocket_horizontal_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.precise_center_y -= self.settings.rocket_vertical_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.precise_center_y += self.settings.rocket_vertical_speed

        # Now make integer change in actual self.rect coordinates
        self.rect.centerx = int(self.precise_center_x)
        self.rect.centery = int(self.precise_center_y)



