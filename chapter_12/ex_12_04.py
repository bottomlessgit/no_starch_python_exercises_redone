import sys

import pygame

# Create empty screen as instructed
screen = pygame.display.set_mode((600, 400))
screen.fill((0, 0, 0))
pygame.display.flip()

# Create loop to print oygame events to console
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key)