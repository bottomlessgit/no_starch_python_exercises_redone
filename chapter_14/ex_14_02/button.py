import pygame

class Button():
    """Clickable user input button"""
    def __init__(self, settings, screen, text):
        """Initialize button"""
        # Set screen to draw to
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Render text
        self.font = pygame.font.SysFont(None, settings.button_font_size, True)
        self.text_image = self.font.render(text, True, settings.button_text_color)
        self.text_image_rect = self.text_image.get_rect()
        # Create background button surface onto which to draw text
        self.image = pygame.Surface(settings.button_dimensions)
        self.image.fill(settings.button_color)
        self.rect = self.image.get_rect()
        self.text_image_rect.center = self.rect.center
        # Now draw text onto button
        self.image.blit(self.text_image, self.text_image_rect)
        # Set button to center of screen
        self.rect.center = self.screen_rect.center


    def blitme(self):
        """Draw button onto screen"""
        self.screen.blit(self.image, self.rect)


    def clicked(self, click_event):
        """Returns True if button was clicked"""
        return self.rect.collidepoint(click_event.pos)