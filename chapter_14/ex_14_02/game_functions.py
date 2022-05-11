import sys
import pygame

from bullet import Bullet


def check_event(event, settings, screen, ship, bullets, stats, start_button, target):
    """Handles responding to user input"""
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        check_keydown_events(event, settings, screen, ship, bullets, stats, target)
    elif event.type == pygame.KEYUP:
        check_keyup_events(event, ship)
    elif event.type == pygame.MOUSEBUTTONDOWN and stats.game_active == False:
        check_start_button(event, start_button, stats, bullets, target, ship)


def check_keydown_events(event, settings, screen, ship, bullets, stats, target):
    """Handles user pressing of keys"""
    if event.key == pygame.K_p and stats.game_active == False:
        initialize_game(bullets, target, stats, ship)
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE and stats.game_active:
        bullets.add(Bullet(settings, screen, ship))



def check_keyup_events(event, ship):
    """Handles user releasing of keys"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_start_button(event, button, stats, bullets, target, ship):
    """Sets game to active if user clicks start button"""
    if button.rect.collidepoint(event.pos):
        initialize_game(bullets, target, stats, ship)

def draw_screen(ship, target, bullets, start_button, stats):
    """Draws all game elements to screen"""
    for bullet in bullets:
        bullet.draw()
    ship.blitme()
    target.draw()
    pygame.display.flip()
    if not stats.game_active:
        start_button.blitme()



def handle_bullets(bullets, target, stats, ship):
    """Handles bullet collisions with target and dissapearance off-screen"""
    for bullet in bullets:
        if bullet.off_screen():
            bullets.remove(bullet)
            stats.misses_left -= 1
            if stats.misses_left == 0:
                stats.game_active = False

    pygame.sprite.spritecollide(target, bullets, True)


def initialize_game(bullets, target, stats, ship):
    """Initalizes all game elements"""
    bullets.empty()
    target.initialize_position()
    ship.initialize_position()
    stats.reinitialize_stats()




