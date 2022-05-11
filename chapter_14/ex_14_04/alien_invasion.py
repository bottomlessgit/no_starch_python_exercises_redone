 import sys
import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    """Function that runs the whole game"""
    # Initialize pygame library
    pygame.init()
    # Create settings object
    settings = Settings()
    # Create game statistics object for changing came level variables
    stats = GameStats(settings)
    # Create game screen 
    screen = pygame.display.set_mode(settings.screen_dimensions)
    # Create controlable player ship
    ship = Ship(settings, screen)
    # Create player scoreboard
    scoreboard = Scoreboard(settings, screen, stats)
    # Create Sprite group to contain bullets shot by ship
    bullets = pygame.sprite.Group()
    # Create Sprite group to contain aliens shot at by ship
    aliens = pygame.sprite.Group()
    # Create game start button
    start_button = Button(settings, screen, settings.button_start_text)


    while True:
        for event in pygame.event.get():
            gf.check_game_event(event, settings, screen, ship, bullets, start_button, stats, aliens, scoreboard)

        if stats.game_active:
            ship.update()
            bullets.update()
            aliens.update()
            gf.check_dead_bullets(bullets)
            gf.check_alien_side_collisions(aliens, settings)
            gf.check_alien_bullet_collisions(aliens, bullets, settings, screen, stats, scoreboard)
            gf.check_fleet_victory(aliens, bullets, ship, settings, screen, stats, scoreboard)
        # Draws all relevant game elements to screen
        gf.update_screen(settings, screen, ship, bullets, aliens, start_button, stats, scoreboard)


run_game()