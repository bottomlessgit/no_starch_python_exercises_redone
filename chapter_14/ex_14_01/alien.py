import pygame

class Alien(pygame.sprite.Sprite):
    """Class to represent alien enemies of ship"""

    # Create class variable image for access by all objects
    # To prevent repetition of loading and scaling image
    IMAGE = None

    def __init__(self, settings, screen):
        super().__init__()
        # Load image to class bariable only if it hasn't been assigned yet
        if Alien.IMAGE == None:
            Alien.IMAGE = pygame.image.load(settings.alien_filename)
            Alien.IMAGE = pygame.transform.scale(Alien.IMAGE, settings.alien_dimensions).convert_alpha()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # For now create rect and precise position variables at default of 0
        # each alien's position will be initialized when alien fleet is created
        self.rect = Alien.IMAGE.get_rect()
        self.precise_x = 0.0
        self.precise_y = 0.0
        # Assign speed from settings
        self.speed_x = settings.alien_speed_x
        self.speed_y = settings.alien_speed_y


    def blitme(self):
        """Draw alien to screen"""
        self.screen.blit(Alien.IMAGE, self.rect)


    def update(self):
        """Updates alien position"""
        self.precise_x += self.speed_x
        self.rect.x = int(self.precise_x)


    def hit_edge(self):
        """Checks if alien at left or right edge of screen"""
        if (self.rect.left < self.screen_rect.left or self.rect.right > self.screen_rect.right):
            return True
        else:
            return False


