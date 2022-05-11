# File to hold useful functions for game
from raindrop import Raindrop


def create_drop(settings, screen, num_row, num_drop):
    """Creates a single drop and positions it"""
    new_drop = Raindrop(settings, screen)
    # Set proper x position
    new_drop.rect.x = (settings.edge_space_x 
                       + num_drop * (settings.drop_width 
                                     + settings.drop_spacing_x))
    # Set proper y position
    new_drop.rect.y = (settings.edge_space_y 
                       + num_row * (settings.drop_height 
                                     + settings.drop_spacing_y))

    # Assign precise_y correct value as well for future updating
    new_drop.precise_y = float(new_drop.rect.y)
    return new_drop



def create_drops(settings, screen, raindrops):
    """Creates a grid of raindrops positioned on screen"""
    for num_row in range(settings.num_rows):
        for num_drop in range(settings.num_drops_in_row):
            # Create new drop
            new_drop = create_drop(settings, screen, num_row, num_drop)
            # Add to raindrop Group
            raindrops.add(new_drop)


def update_drops(raindrops, settings):
    # Update raindrop position
    raindrops.update()

    for drop in raindrops:
        # Check if top of drop is below screen
        if drop.off_screen():
            drop.rect.y = settings.edge_space_y
            drop.precise_y = float(drop.rect.y)

    for drop in raindrops:
        drop.blitme()


def update_screen(screen, settings, raindrops):
    """Function to update screen"""
    screen.fill(settings.screen_color)
    update_drops(raindrops, settings)