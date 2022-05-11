import pygame

class Bullet(pygame.sprite.Sprite):
    """Class to represent bullets shot by ship"""
    def __init__(self, settings, screen, ship):
        # Initialize sprite super
        super().__init__()
        self.screen = screen
        self.color = settings.bullet_color
        #self.dimensions = settings.bullet_dimensions
        self.speed = settings.bullet_speed
        # Initially create bullet at 0 position
        self.rect = pygame.rect.Rect((0, 0), settings.bullet_dimensions)
        # Then position bullet at top center of ship
        self.rect.top = ship.rect.top
        self.rect.center = ship.rect.center
        # Create precise y value for precise decimal movement
        self.precise_y = float(self.rect.y)


    def update(self):
        """Update position of bullet on screen"""
        self.precise_y -= self.speed
        self.rect.y = int(self.precise_y)


    def draw_me(self):
        """Draws bullet to screen as rectangle"""
        pygame.draw.rect(self.screen, self.color, self.rect)


    def is_off_screen(self):
        """Checks if bullet has gone off screen"""
        return bullet.rect.bottom < screen.rect.top
