import sys
import pygame
from bullet import Bullet
from alien import Alien
"""
Module for functions that manipulate the elements of the game. Primarily
deals with game-level functionality, like user input, sprite groups,
and collisions between game elements
"""


def check_event(event, settings, screen, ship, bullets, stats, start_button):
    """Handles a user input event"""
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if not stats.game_active:
            press_start_button(event, stats, start_button)
    elif event.type == pygame.KEYDOWN:
        check_keydown_event(event, settings, screen, ship, bullets, stats)
    elif event.type == pygame.KEYUP:
        check_keyup_event(event, settings, screen, ship)

def check_keydown_event(event, settings, screen, ship, bullets, stats):
    """Handles responses to user pressing key"""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        stats.game_active = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)


def check_keyup_event(event, settings, screen, ship):
    """Handles responses to user releasing key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def  press_start_button(event, stats, start_button):
    if start_button.rect.collidepoint(event.pos):
        stats.game_active = True


def fire_bullet(settings, screen, ship, bullets):
    """Fires bullet from ship"""
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)


def update_screen(settings, screen, ship, bullets, aliens, start_button, stats):
    """Updates all screen elements"""
    # Fill screen with color to erase previous image
    screen.fill(settings.bg_color)
    # Draw game elements if game is active
    if stats.game_active:
        ship.blitme()
        for bullet in bullets:
            bullet.draw_me()
        for alien in aliens:
            alien.blitme()
    # Else draw button
    else:
        start_button.blitme()

    # Load display from pygane buffer
    pygame.display.flip()


def create_fleet(settings, screen, aliens):
    """Creates new fleet positioned at top left corner"""
    for row in range(settings.num_rows):
        for col in range(settings.num_aliens_in_row):
            new_alien = create_alien(settings, screen, row, col)
            aliens.add(new_alien)


def create_alien(settings, screen, row, col):
    """Creates alien at position corresponding to row and column number"""
    new_alien = Alien(settings, screen)
    new_alien.rect.x = col * (settings.alien_spacing_x + settings.alien_width)
    new_alien.rect.y = row * (settings.alien_spacing_y + settings.alien_height)
    new_alien.precise_x = float(new_alien.rect.x)
    new_alien.precise_y = float(new_alien.rect.y)
    return new_alien

def reverse_fleet(aliens):
    """Moves fleet down the screen and reverses its x-direction"""
    for alien in aliens:
        alien.speed_x *= -1
        alien.precise_y += alien.speed_y
        alien.rect.y = int(alien.precise_y)
        # Now update with new speed to ensure alien is in screen bounds
        alien.update()


def check_fleet_reversal(aliens):
    """Reverses alien fleet if any alien hits left or right edge of screen"""
    for alien in aliens:
        if alien.hit_edge():
            # Reverse alien 
            reverse_fleet(aliens)
            break

def handle_bullet_alien_collisions(bullets, aliens, screen, settings):
    """Handles bullet alien collisions"""
    yeet = pygame.sprite.groupcollide(bullets, aliens, True, True)
    yeet = 0
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, aliens)


def check_dead_bullets(bullets):
    """Gets rid of off screen_bullets"""
    for bullet in bullets:
        if bullet.is_off_screen():
            bullets.remove(bullet)


def handle_alien_attack(ship, aliens, bullets, screen, settings, stats):
    """Handles case where aliens collide with ship or reach bottom of screen"""
    if alien_hit_bottom(aliens) or pygame.sprite.spritecollideany(ship, aliens):
        bullets.empty()
        aliens.empty()
        stats.ships_left -= 1
        if stats.ships_left > 0:
            create_fleet(settings, screen, aliens)
        else:
            stats.reset_stats()





def alien_hit_bottom(aliens):
    """Returns true if alien hits bottom of screen"""
    for alien in aliens:
        if alien.rect.bottom > alien.screen_rect.bottom:
            return True
    return False











