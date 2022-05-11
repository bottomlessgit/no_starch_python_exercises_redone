import sys

import pygame

# Initialize pygame
pygame.init()

# Set game dimension and get screen surface
screen = pygame.display.set_mode((1200, 800))

# Fill surface with color blue
bg_color = (0, 0, 200)
screen.fill(bg_color)

# Load new drawn screen from pygame display buffer
pygame.display.flip()

# Check for events until user quits
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit when user quits
            sys.exit()