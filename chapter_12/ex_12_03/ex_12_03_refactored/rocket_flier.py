# This version will not be refactored for simplicity
import sys

import pygame

from settings import Settings

from rocket import Rocket

import game_functions as gf


# Initialize pygame library
pygame.init()

# Make settings object
settings = Settings()

# Create and size display screen surface
screen = pygame.display.set_mode(settings.game_size)
screen_rect = screen.get_rect()

# Fill with chosen background color
screen.fill(settings.bg_color)

# Create Rocket object
rocket = Rocket(settings, screen)


while True:
    # Handle input events
    gf.check_events(rocket)

    # Now handle ship movement
    rocket.update()

    # Fill screen with background color
    screen.fill(settings.bg_color)
    # Draw rocket to screen in new position
    screen.blit(rocket.image, rocket.rect)
    # Load from pygame screen buffer to display
    pygame.display.flip()


