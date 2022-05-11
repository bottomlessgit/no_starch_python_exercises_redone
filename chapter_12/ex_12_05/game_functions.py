import sys

import pygame
from bullet import Bullet

def check_events(rocket, settings, screen, ship, bullets):
    """Checks for and handles all user input events"""
    for event in pygame.event.get():
        # Exit if user quits
        if event.type == pygame.QUIT:
            sys.exit()
        # Change movement flags if arrow key goes up or down
        if event.type == pygame.KEYDOWN:
            check_keydown_events(rocket, settings, screen, ship, bullets, event)
        if event.type == pygame.KEYUP:
            check_keyup_events(rocket, event)


def check_keydown_events(rocket, settings, screen, ship, bullets, event):
    """Handles keydown events"""
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True
    if event.key == pygame.K_SPACE and len(bullets) < settings.bullet_limit:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)



def check_keyup_events(rocket, event):
    """Handles keyup events"""
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False


def update_bullets(bullets):
    """Updates bullets positions and deletes bullets that reach screen end"""
    # Update bullet positions
    bullets.update()
    for bullet in bullets:
        if(bullet.rect.right > bullet.screen_rect.right):
            bullets.remove(bullet)


def update_screen(screen, settings, rocket, bullets):
    """Update all screen elements"""
    # Fill screen with background color
    screen.fill(settings.bg_color)
    # Draw rocket to screen in new position
    screen.blit(rocket.image, rocket.rect)
    # Update bullet positions
    update_bullets(bullets)
    # Draw bullets onto screen
    for bullet in bullets:
        bullet.draw_bullet()
    # Load from pygame screen buffer to display
    pygame.display.flip()

