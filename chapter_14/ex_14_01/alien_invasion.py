import cProfile
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from gamestats import GameStats
from button import Button
import game_functions as gf

def run_game():
    """Runs alien invasion game"""
    # Initialize pygame
    pygame.init()
    # Create settings object
    settings = Settings()
    # Create stats object
    stats = GameStats(settings)
    # Initialize display
    screen = pygame.display.set_mode((settings.screen_dimensions))
    # Create ship object
    ship = Ship(settings, screen)
    # Create sprite groups for bullets and aliens
    bullets = Group()
    aliens = Group()
    # Create start button
    start_button_text = "Start"
    start_button = Button(settings, screen, start_button_text, settings.button_dimensions)
    # Create initial fleet of aliens
    gf.create_fleet(settings, screen, aliens)


    while True:
        for event in pygame.event.get():
            gf.check_event(event, settings, screen, ship, bullets, stats, start_button)

        if stats.game_active:
            ship.update()
            bullets.update()
            aliens.update()
            gf.handle_bullet_alien_collisions(bullets, aliens, screen, settings)

            gf.check_fleet_reversal(aliens)
            gf.handle_alien_attack(ship, aliens, bullets, screen, settings, stats)

        # Update the screen to reflect changes
        gf.update_screen(settings, screen, ship, bullets, aliens, start_button, stats)
        




run_game()
#cProfile.run('run_game()')