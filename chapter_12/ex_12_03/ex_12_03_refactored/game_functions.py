import pygame

import sys


def check_events(rocket):
    """Checks for and handles all user input events"""
    for event in pygame.event.get():
        # Exit if user quits
        if event.type == pygame.QUIT:
            sys.exit()
        # Change movement flags if arrow key goes up or down
        if event.type == pygame.KEYDOWN:
            check_keydown_events(rocket, event)
        if event.type == pygame.KEYUP:
            check_keyup_events(rocket, event)


def check_keydown_events(rocket, event):
    """Handles keydown events"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    if event.key == pygame.K_LEFT :
        rocket.moving_left = True
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True


def check_keyup_events(rocket, event):
    """Handles keyup events"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    if event.key == pygame.K_LEFT :
        rocket.moving_left = False
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False