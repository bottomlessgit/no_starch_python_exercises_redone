"""This version of catch.py uses a group to hold the 
balls (even though the standard is to have one)"""
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
balls = pygame.sprite.Group()
gf.initialize_balls(settings, screen, balls)


while True:
    # Check for user events
    for event in pygame.event.get():
        gf.check_event(event, catcher)
    # Update positions of game elements
    gf.update_game_elements(catcher, balls, settings, screen)
    # Update screen
    gf.update_screen(screen, settings, catcher, balls)

