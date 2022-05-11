import pygame

class Catcher(pygame.sprite.Sprite):
    """Class representing catcher element in game"""
    def __init__(self, settings, screen):
        """Initializes catcher object at bottom center of screen"""
        
        # Initialize sprite superclass
        super().__init__()

        # Give object game screen to be drawn to
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Load image
        self.image = pygame.image.load(settings.catcher_filename)
        # Set image to chosen dimensions
        self.image = pygame.transform.scale(
            self.image, 
            (settings.catcher_width, settings.catcher_height))

        # Initialize position at bottom center of screen
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Set precise(float) value for x for precision movement
        self.precise_x = float(self.rect.x)

        # Initialize moving flags as False
        self.moving_right = False 
        self.moving_left = False
        self.speed = settings.catcher_speed

    def update(self):
        """Updates catcher position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.precise_x += self.speed
            self.rect.x = int(self.precise_x)

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.precise_x -= self.speed
            self.rect.x = int(self.precise_x)

    def blitme(self):
        """Draws ball to screen"""
        self.screen.blit(self.image, self.rect)

