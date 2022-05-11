# This version will not be refactored for simplicity
import sys

import pygame

# Initialize pygame library
pygame.init()

# Create and size display screen surface
screen = pygame.display.set_mode((1200,800))
screen_rect = screen.get_rect()

# Fill with chosen background color
bg_color = (0, 0, 0)
screen.fill(bg_color)

rocket = pygame.image.load("rocket.bmp")
# NOTE: The scale function hasn't been used in the textbook. The rocket img
# was too large, so I use this function to scale it down to a smaller surface
rocket = pygame.transform.scale(rocket, (100, 100))


rocket_rect = rocket.get_rect()

# Initialize positoion
rocket_rect.centerx = screen_rect.centerx
rocket_rect.centery = screen_rect.centery

# Create precise x y position attributes for oprecise movement
precise_center_x = float(rocket_rect.centerx)
precise_center_y = float(rocket_rect.centery)

# Create standard rocket speeds for x and y movement
rocket_horizontal_speed = 1.0
rocket_vertical_speed = 1.5

# Flags to keep track of how rocket should move
moving_right = False
moving_left = False
moving_up = False
moving_down = False


while True:
    for event in pygame.event.get():
        # Exit if user quits
        if event.type == pygame.QUIT:
            sys.exit()
        # Change movement flags if arrow key goes up or down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT :
                moving_left = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT :
                moving_left = False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False

    # Now handle movement
    if moving_right and rocket_rect.right < screen_rect.right:
        precise_center_x += rocket_horizontal_speed
    if moving_left and rocket_rect.left > screen_rect.left:
        precise_center_x -= rocket_horizontal_speed
    if moving_up and rocket_rect.top > screen_rect.top:
        precise_center_y -= rocket_vertical_speed
    if moving_down and rocket_rect.bottom < screen_rect.bottom:
        precise_center_y += rocket_vertical_speed

    # Now make integer change in actual rocket_rect coordinates
    rocket_rect.centerx = int(precise_center_x)
    rocket_rect.centery = int(precise_center_y)

    # Fill screen with background color
    screen.fill(bg_color)
    # Draw rocket to screen in new position
    screen.blit(rocket, rocket_rect)
    # Load from pygame screen buffer to display
    pygame.display.flip()


