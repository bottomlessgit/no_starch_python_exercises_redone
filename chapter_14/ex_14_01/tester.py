import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Runs alien invasion game"""
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    # Create settings object
    blork = pygame.image.load("alien.bmp")
    rect1 = blork.get_rect()
    rect2 = blork.get_rect()

    rect1.x = 100
    rect1.y = 100
    rect2.x = 700
    rect2.y = 700

    screen.fill((0, 0, 0))

    screen.blit(blork, rect1)
    screen.blit(blork, rect2)
    pygame.display.flip()




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

run_game()