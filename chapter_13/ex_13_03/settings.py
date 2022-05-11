import pygame

class Settings():
    """Class to keep track of relevant settings"""
    def __init__(self):
        """Initialize settings object"""
        # Screen size settings
        self.screen_dimensions = (1200, 800)
        self.screen_color = (0, 0, 0)

        # Raindrop settings
        self.drop_filename = "raindrop.bmp"
        self.drop_width = 60
        self.drop_height = 100
        self.drop_speed = 1.5
        self.drop_spacing_x = 30
        self.drop_spacing_y = 50
        self.edge_space_x = 10
        self.edge_space_y = 10

        """
        To save space and the repetition of effort, and because each raindrop 
        is the same size, I load and scale the image in settings, and pass the
        same image to every instance of the Raindrop class
        """
        # Load image
        self.drop_image = pygame.image.load(self.drop_filename)
        # Scale image
        self.drop_image = pygame.transform.scale(self.drop_image, (self.drop_width, self.drop_height))

        # Calculations for number of rows and colums of raindrops
        space_for_drops_x = self.screen_dimensions[0] - 2 * self.edge_space_x + self.drop_spacing_x
        self.num_drops_in_row = int(space_for_drops_x / (self.drop_width + self.drop_spacing_x))

        space_for_drops_y = self.screen_dimensions[1] - 2 * self.edge_space_y
        self.num_rows = int(space_for_drops_y / (self.drop_height + self.drop_spacing_y))


        print(self.num_rows)
