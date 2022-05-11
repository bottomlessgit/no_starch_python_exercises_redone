import pygame

class Raindrop(pygame.sprite.Sprite):
    """Class represeting raindrop to be drawn to screen"""
    def __init__(self, settings, screen):
        """Initializes raindrop object"""
        # Initialize sprite sttributes
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = settings.drop_image
        # Initialize rect, drop will be positioned by ccreate_drops function
        self.rect = self.image.get_rect()
        self.speed = settings.drop_speed
        # precise_y is initialized
        self.precise_y = 0.0


    def update(self):
        """Update the position of the raindrop"""
        self.precise_y += self.speed
        self.rect.y = int(self.precise_y)

    def blitme(self):
        """Draw raindrop to screen"""
        self.screen.blit(self.image, self.rect)

    def off_screen(self):
        """Checks if randrop is off-screen"""
        if self.rect.top > self.screen_rect.bottom:
            return True
        else:
            return False


