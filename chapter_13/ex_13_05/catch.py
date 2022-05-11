import pygame
from settings import Settings
from catcher import Catcher
from ball import Ball
import game_functions as gf


# Initialize pygame library
pygame.init()

# Game settings
settings = Settings()

# Initialize screen
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

# Initialize game elements
catcher = Catcher(settings, screen)
ball = Ball(settings, screen)

while True:
    # Check for user events
    for event in pygame.event.get():
        gf.check_event(event, catcher)
    # Update positions of game elements
    gf.update_game_elements(catcher, ball, settings, screen)
    # Handle case where ball must be replaced
    if gf.handle_ball(catcher, ball, settings, screen):
        ball = Ball(settings, screen)
    # Update screen
    gf.update_screen(screen, settings, catcher, ball)

