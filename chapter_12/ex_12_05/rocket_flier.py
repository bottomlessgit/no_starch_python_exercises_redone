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

# Create group to hold bullet sprites
bullets = pygame.sprite.Group()


while True:
    # Handle input events
    gf.check_events(rocket, settings, screen, rocket, bullets)

    # Now handle rocket movement
    rocket.update()
    # Update bullet positions
    gf.update_bullets(bullets)
    # Draw all screen elements to screen
    gf.update_screen(screen, settings, rocket, bullets)



