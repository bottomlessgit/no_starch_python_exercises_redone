import sys

import pygame

# Initialize pygame
pygame.init()

# Initialize screen
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Set background color
bg_color = (0, 0, 0)  # Black
screen.fill(bg_color)

# Load star image:
star = pygame.image.load("star.bmp")
# Scale star to given size
star_width = 40
star_height = 40
star = pygame.transform.scale(star, (star_width, star_height))

# Choose distance between stars
dist_x = 40
dist_y = 40

# Choose minimum edge distance between stars and edge
min_edge_dist_x = 20
min_edge_dist_y = 20

# Find number of stars in a row
width_for_stars = screen_width - 2 * min_edge_dist_x - star_width
num_stars_in_row = int(width_for_stars / (star_width + dist_x)) + 1
edge_dist_x = int((screen_width - num_stars_in_row * (star_width + dist_x) + dist_x) / 2)

# Find number of rows:
height_for_stars = screen_height - 2 * min_edge_dist_y - star_height
num_rows = int(height_for_stars / (star_height + dist_y)) + 1
edge_dist_y = int((screen_height - num_rows * (star_height + dist_y) + dist_y) / 2)


for num_row in range(num_rows):
    for num_star in range(num_stars_in_row):
        star_x = edge_dist_x + num_star * (star_width + dist_x)
        star_y = edge_dist_y + num_row * (star_height + dist_y)
        screen.blit(star, (star_x, star_y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()






# find amount of width between star and screen edge for centering stars
