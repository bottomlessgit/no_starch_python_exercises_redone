import sys

import pygame
import auxiliary_functions as af
from settings import Settings
from raindrop import Raindrop


# Initialize pygame
pygame.init()

# Initialize settings object to pass to 
settings = Settings()

# Initialize screen
screen = pygame.display.set_mode(settings.screen_dimensions)

# Create group for raindrops
raindrops = pygame.sprite.Group()

# create raindrops
af.create_drops(settings, screen, raindrops)


# Create while loop that only quits with user exit command
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    af.update_screen(screen, settings, raindrops)
    # Load new screen from pygame buffer
    pygame.display.flip()




