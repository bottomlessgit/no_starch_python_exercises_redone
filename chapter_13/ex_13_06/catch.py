"""This version of catch.py uses a group to hold the 
balls (even though the standard is to have one)"""
import pygame
from settings import Settings
from catcher import Catcher
from ball import Ball
from game_stats import GameStats
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

# Initialize running stats
game_stats = GameStats(settings)


while True:
    # Check for user events
    for event in pygame.event.get():
        gf.check_event(event, catcher)
    # Only continue updating if player hasn't missed too many balls
    if game_stats.game_active:
        # Update positions of game elements
        gf.update_game_elements(catcher, balls, settings, screen, game_stats)
        # Update screen
        gf.update_screen(screen, settings, catcher, balls)

