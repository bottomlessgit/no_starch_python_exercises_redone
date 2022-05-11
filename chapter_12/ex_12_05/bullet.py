import pygame

class Bullet(pygame.sprite.Sprite):
    """Class to represent bullet element"""
    def __init__(self, settings, screen, rocket):
        """Initialize bullet object"""
        # use Sprite superclass constructor
        super().__init__()
        # Take size and speed from settings object
        self.width = settings.bullet_width # x length
        self.height = settings.bullet_height # y length
        self.speed = settings.bullet_speed
        self.color = settings.bullet_color

        # Assign screen to draw to
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Create Rect then position later 
        # (since constructor only takes left and top)
        self.rect = pygame.rect.Rect(0, 0, self.width, self.height)

        # Assign initial position from rocket location
        self.rect.right = rocket.rect.right
        self.rect.centery = rocket.rect.centery

        # Give precise x-value for precise speed movement
        self.precise_center_x = float(self.rect.centerx)

    def update(self):
        """Updates the position and state of the bullet"""
        self.precise_center_x += self.speed
        self.rect.centerx = int(self.precise_center_x)

    def draw_bullet(self):
        """Draw bullet to game screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)




        