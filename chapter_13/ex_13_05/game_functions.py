# File to hold functions that help the game operate
from sys import exit

import pygame
from ball import Ball

def check_event(event, catcher):
    """Checks for and responds to a user input event"""
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        check_keydown_event(event, catcher)
    elif event.type == pygame.KEYUP:
        check_keyup_event(event, catcher)


def check_keydown_event(event, catcher):
    """Handles keydown events"""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    if event.key == pygame.K_LEFT:
        catcher.moving_left = True


def check_keyup_event(event, catcher):
    """Handles keydown events"""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = False
    if event.key == pygame.K_LEFT:
        catcher.moving_left = False


def handle_ball(catcher, ball, settings, screen):
    """Creates new randomly positions ball if ball and catcher colide"""
    if pygame.sprite.collide_rect(catcher, ball) or ball.is_off_screen():
        return True
    else:
        return False

def update_game_elements(catcher, ball, settings, screen):
    """Updates game elements positions and creates new ball if needed"""
    ball.update()
    catcher.update()

def update_screen(screen, settings, catcher, ball):
    """Updates screen"""
    screen.fill(settings.bg_color)
    ball.blitme()
    catcher.blitme()
    pygame.display.flip()
