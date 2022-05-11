import sys

import pygame
from settings import Settings
from ship import Ship
from target import Target
from game_stats import GameStats
from button import Button
import game_functions as gf

def run_game():
    """Game where player shoots bullets at target until 3 misses"""
    # initialize pygame
    pygame.init()
    # Create settings object to pass to game objects
    settings = Settings()
    # Create gamestats object
    stats = GameStats(settings)
    # Create screen object
    screen = pygame.display.set_mode(settings.screen_dimensions)
    # Create ship
    ship = Ship(settings, screen)
    # Create moving target
    target = Target(settings, screen)
    # Create group for bullets
    bullets = pygame.sprite.Group()
    # Create start button
    start_button = Button(settings, screen, settings.start_button_text)



    while True:
        for event in pygame.event.get():
            gf.check_event(event, settings, screen, ship, bullets, stats, start_button, target)

        if stats.game_active:
            gf.handle_bullets(bullets, target, stats, ship)
            ship.update()
            target.update()
            bullets.update()
            screen.fill(settings.screen_color)



        gf.draw_screen(ship, target, bullets, start_button, stats)



run_game()
