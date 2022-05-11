import pygame

class Ship(pygame.sprite.Sprite):
    """Class that repreents controllable player ship"""
    def __init__(self, settings, screen):
        """Initialize ship object"""
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(settings.ship_filename)
        # Scale image to size specified in settings
        self.image = pygame.transform.scale(self.image, settings.ship_dimensions).convert_alpha()
        self.rect = self.image.get_rect()
        # Initially position ship at bottom center of screen
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom
        # Create precise x position for decimal precision movement
        self.precise_x = float(self.rect.x)
        # Give personal speed 
        self.speed = settings.ship_speed
        # Create moving flags
        self.moving_right = False
        self.moving_left = False



    def update(self):
        """Updates position on screen"""
        # Update precise_x based on movement flags and position on screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.precise_x += self.speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.precise_x -= self.speed
        # Assign precise x value to rect value for drawing to screen
        self.rect.x = int(self.precise_x)


    def blitme(self):
        """Draws ship to screen"""
        self.screen.blit(self.image, self.rect)


