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

        # Also rotated image using rotate function from tranform module
        self.image = pygame.transform.rotate(self.image, 270)

        # get rect of screen for positioning
        self.screen_rect = self.screen.get_rect()

        # Get rect for changing rocket position
        self.rect = self.image.get_rect()

        # Initialize positoion
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Create precise x y position attributes for oprecise movement
        self.precise_center_y = float(self.rect.centery)


        # Flags to keep track of how rocket should move
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update Rocket position based on movement flags and position"""
        # Now handle movement
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.precise_center_y -= self.settings.rocket_vertical_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.precise_center_y += self.settings.rocket_vertical_speed

        # Now make integer change in actual self.rect coordinates
        self.rect.centery = int(self.precise_center_y)



