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


def initialize_balls(settings, screen, balls):
    """Fills balls sprite group with number of balls specified in settings"""
    for new_ball in range(settings.num_balls):
        balls.add(Ball(settings, screen))


def handle_balls(catcher, balls, settings, screen):
    """Creates new randomly positions ball if ball and catcher colide"""
    # Remove any balls that collide with catcher
    caught_balls = pygame.sprite.spritecollide(catcher, balls, True)
    for new_ball in range(len(caught_balls)):
        balls.add(Ball(settings, screen))
    # Remove balls that fall off screen
    for ball in balls:
        if ball.rect.top > ball.screen_rect.bottom:
            balls.remove(ball)
            balls.add(Ball(settings, screen))

def update_game_elements(catcher, balls, settings, screen):
    """Updates game elements positions and creates new balls if needed"""
    handle_balls(catcher, balls, settings, screen)
    balls.update()
    catcher.update()

def update_screen(screen, settings, catcher, balls):
    """Updates screen"""
    screen.fill(settings.bg_color)
    for ball in balls.sprites():
        ball.blitme()
    catcher.blitme()
    pygame.display.flip()
