import pygame

class Bullet(pygame.sprite.Sprite):
    """Class to represent bullets ship from ship at target"""
    def __init__(self, settings, screen, ship):
        """Initializes bullet object"""
        # Initialize Sprite superclass
        super().__init__()
        # Assign screen to print to
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Assign ship to shoot from
        self.ship_rect = ship.rect
        # Create rect at arbitrary position then set position to ship center
        self.rect = pygame.Rect((0, 0), settings.bullet_dimensions)
        self.rect.right = self.ship_rect.right
        self.rect.centery = self.ship_rect.centery
        # Set precise floating point value for x for precise movement
        self.precise_x = float(self.rect.x)
        # Set color and speed
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed


    def update(self):
        """Updates position of bullet"""
        self.precise_x += self.speed
        self.rect.x = int(self.precise_x)


    def draw(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


    def off_screen(self):
        """Checks if bullet is off right side of screen"""
        return self.rect.left > self.screen_rect.right

