import pygame
from random import randint

class Ball(pygame.sprite.Sprite):
    """Class representing ball element in game"""
    def __init__(self, settings, screen):
        """Initializes ball object at bottom center of screen"""

        # Give object game screen to be drawn to
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.settings = settings

        # Load image
        self.image = pygame.image.load(settings.ball_filename)
        # Set image to chosen dimensions
        self.image = pygame.transform.scale(
            self.image, 
            (settings.ball_width, settings.ball_height))

        # Initialize random position at top of screen
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0, self.screen_rect.right - self.rect.width)
        self.rect.top = self.screen_rect.top
        # Set precise(float) value for x for precision movement
        self.precise_y = float(self.rect.y)

        self.speed = settings.ball_speed


    def update(self):
        """Updates ball position"""
        self.precise_y += self.speed
        self.rect.y = int(self.precise_y)
        # Handle case where ball goes off screen


    def is_off_screen(self):
        return self.rect.top > self.screen_rect.bottom

    def blitme(self):
        """Draws ball to screen"""
        self.screen.blit(self.image, self.rect)

    