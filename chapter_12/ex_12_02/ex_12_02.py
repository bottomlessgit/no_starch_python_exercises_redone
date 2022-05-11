import sys

import pygame

# Initialize pygame
pygame.init()

# Set display size and get screen surface object
screen = pygame.display.set_mode((1200,800))
screen_rect = screen.get_rect()
# Fill with black to match pacman.bmp background
screen.fill((0, 0, 0))

# Load image and set center to screen center
pacman_surface = pygame.image.load("pacman.bmp")
pacman_rect = pacman_surface.get_rect()
pacman_rect.center = screen_rect.center

# Draw to screen and load display from buffer
screen.blit(pacman_surface, pacman_rect)
pygame.display.flip()

# Event loop to monitor for quit event
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()