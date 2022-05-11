"""A module for functions game-level functions, handling user input,
sprite group interactions, and sprite collisions"""
import sys
import pygame
from alien import Alien
from bullet import Bullet



def check_game_event(event, settings, screen, ship, bullets, start_button, stats, aliens, scoreboard):
    """Handles user input events"""
    if event.type == pygame.QUIT:
        quit_game(stats)
    elif event.type == pygame.KEYDOWN:
        check_keydown_event(event, settings, screen, ship, bullets, stats, aliens, scoreboard)
    elif event.type == pygame.KEYUP:
        check_keyup_events(event, ship)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if not stats.game_active:
            check_button_clicked(event, start_button, stats, settings, screen, ship, bullets, aliens, scoreboard)



def check_keydown_event(event, settings, screen, ship, bullets, stats, aliens, scoreboard):
    """Handles keydown events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE and stats.game_active:
        bullets.add(Bullet(settings, screen, ship))
    elif event.key == pygame.K_p:
        reset_game(settings, screen, ship, bullets, aliens, stats, scoreboard)
        stats.game_active = True
    elif event.key == pygame.K_q:
        quit_game(stats)

def check_keyup_events(event, ship):
    """Handles keyup events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_mousbuttondown_events(event, settings, screen, ship, bullets, start_button, stats, aliens, scoreboard):
    """Handles mouseclickdown events"""
    if not stats.game_active:
        check_button_clicked(event, start_button, stats, settings, screen, ship, bullets, aliens, scoreboard)

def create_fleet(settings, screen, aliens):
    """Creates new fleet of aliens positioned at top left corner of screen"""
    # Calculate total alien space in x and y axes and add to position for each loop
    alien_x = 0
    alien_y = 0
    total_alien_width = settings.alien_width + settings.alien_spacing_x
    total_alien_height = settings.alien_height + settings.alien_spacing_y
    for row in range(settings.num_rows_in_fleet):
        for col in range(settings.num_aliens_in_row):
            # Add alien to fleet group
            aliens.add(create_alien(settings, screen, alien_x, alien_y))
            # Change alien_x coordinate
            alien_x += total_alien_width
        # Change alien_y coordinate
        alien_y += total_alien_height
        # Reset alien_x coordinate for new row
        alien_x = 0

def create_alien(settings, screen, alien_x, alien_y):
    """Creates a new alien at the given coordinates"""
    # Create alien
    new_alien = Alien(settings, screen)
    # Set rect coordinates
    new_alien.rect.x = alien_x
    new_alien.rect.y = alien_y
    # Set precise coordinates
    new_alien.precise_x = float(new_alien.rect.x)
    new_alien.precise_y = float(new_alien.rect.y)
    return new_alien



def check_alien_side_collisions(aliens, settings):
    """Checks if any alien hits side of screen and reverses fleet direction
    and moves the fleet downwards if so"""
    for alien in aliens:
        if alien.hit_side():
            # Reverse direction
            settings.alien_x_speed *= -1
            # Move fleet down
            move_fleet_down(aliens)
            # Now break as not to repeat
            break


def move_fleet_down(aliens):
    """Moves fleet down the screen"""
    for alien in aliens:
        alien.move_down_screen()




def check_alien_bullet_collisions(aliens, bullets, settings, screen, stats, scoreboard):
    """Checks for alien bullet collisions"""
    # Remove collided elements
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # Increase score based on number of aliens killed
    if collisions:
        for alien_list in collisions.values():
            stats.score_increase(len(alien_list))
        scoreboard.refresh_score_surface()


    if len(aliens) == 0:
        fleet_defeat(aliens, bullets, settings, screen, stats, scoreboard)


def fleet_defeat(aliens, bullets, settings, screen, stats, scoreboard):
    """Handles case where a fleet of aliens is defeated"""
    bullets.empty()
    settings.next_level()
    stats.level += 1
    scoreboard.refresh_level_surface()
    create_fleet(settings, screen, aliens)


def check_fleet_victory(aliens, bullets, ship, settings, screen, stats, scoreboard):
    """Checks if alien collided with ship or bottom of screen
    and responds accordingly"""
    if fleet_bottom_collision(aliens) or pygame.sprite.spritecollide(ship, aliens, False):
        stats.lives -= 1
        scoreboard.refresh_lives_surface()

        if stats.lives == 0:
            stats.game_active = False
            stats.set_high_score()

        else:
            bullets.empty()
            aliens.empty()
            create_fleet(settings, screen, aliens)


def fleet_bottom_collision(aliens):
    """Returns true if any alien hits the bottom of the screen"""
    for alien in aliens:
        if alien.hit_bottom():
            return True
    return False


def update_screen(settings, screen, ship, bullets, aliens, start_button, stats, scoreboard):
    """Updates screen based on game state"""
    screen.fill(settings.screen_color)
    # If game is active draw game elements
    for bullet in bullets:
        bullet.draw()
    ship.blitme()
    for alien in aliens:
        alien.draw()
    # Else draw start button
    if not stats.game_active:
        start_button.blitme()

    scoreboard.draw()

    pygame.display.flip()

def check_button_clicked(event, start_button, stats, settings, screen, ship, bullets, aliens, scoreboard):
    """Sets game_active to true if button clicked"""
    if start_button.rect.collidepoint(event.pos):
        reset_game(settings, screen, ship, bullets, aliens, stats, scoreboard)
        stats.game_active = True


def check_dead_bullets(bullets):
    """Removes bullets that have gone off screen"""
    for bullet in bullets:
        if bullet.off_screen():
            bullets.remove(bullet)


def reset_game(settings, screen, ship, bullets, aliens, stats, scoreboard):
    """Resets all game elements to starting positions and values"""
    settings.set_default_settings()
    ship.initialize_ship_position()
    stats.reset_stats()
    bullets.empty()
    aliens.empty()
    create_fleet(settings, screen, aliens)
    scoreboard.refresh()


def quit_game(stats):
    """Loads high score into file and quits game"""
    stats.set_high_score()
    stats.save_high_score()
    sys.exit()





