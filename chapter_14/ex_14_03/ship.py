import pygame

class Ship():
    """Class representing controllable player ship that shoots bullets"""
    def __init__(self, settings, screen):
        """Initializes ship object"""
        # Assign screen to draw to
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Load in image, rotate, and scale the ship image
        self.image = pygame.image.load(settings.ship_filename)
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, settings.ship_dimensions)
        # Get ship Rect and Position ship at center left of screen
        self.rect = self.image.get_rect()
        # Set ship position stats to game start position
        self.initialize(settings)
        # Set movement flags for controlling movement
        self.moving_up = False
        self.moving_down = False
        # Set speedup factor
        self.speedup_factor = settings.ship_speedup_factor


    def initialize(self, settings):
        """Set ship position stats to game start position and resets speed"""
        # Get ship Rect and Position ship at center left of screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left  = self.screen_rect.left
        # Create precise (floating point) value for y for precise position assignment
        self.precise_y = float(self.rect.y)
        # Set speed
        self.speed = settings.ship_speed


    def update(self):
        """Updates position of ship based on movement flags and position on screen"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.precise_y -= self.speed
            self.rect.y = int(self.precise_y)
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.precise_y += self.speed
            self.rect.y = int(self.precise_y)


    def speedup(self):
        """Speeds up ship by specified factor"""
        self.speed *= self.speedup_factor


    def blitme(self):
        self.screen.blit(self.image, self.rect)