import pygame

class Target(pygame.sprite.Sprite):
    """Class to represent moving target user tries to shoot"""
    def __init__(self, settings, screen):
        """Initialize Target object"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.color = settings.target_color
        # Create new rect to draw by filling with color
        self.rect = pygame.Rect((0, 0), settings.target_dimensions)
        # Set target position stats to game start position and set default speed
        self.initialize(settings)
        # Set speedup factor
        self.speedup_factor = settings.target_speedup_factor
        

    def initialize(self, settings):
        """Set Target position stats to game start position"""
        # Position rect at right center of screen
        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery
        # Set precise floating point value for y for precise movement
        self.precise_y = float(self.rect.y)
        # Set speed
        self.speed = settings.target_speed


    def speedup(self):
        """Speeds up ship by specified factor"""
        self.speed *= self.speedup_factor


    def update(self):
        """Update position of rectangle on screen"""
        self.precise_y += self.speed
        self.rect.y = int(self.precise_y)
        if self.hit_screen_edge():
            self.speed *= -1


    def draw(self):
        """Draw target rectangle to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)



    def hit_screen_edge(self):
        return (self.rect.top < self.screen_rect.top 
                or self.rect.bottom > self.screen_rect.bottom)
