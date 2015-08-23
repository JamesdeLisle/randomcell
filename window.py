__author__ = 'Shed'

import pygame

class grid_window:
    """A window, on which a grid will be drawn"""

    def __init__(self, width, height):
        self.margin = 100
        self.square_size = 20
        # TODO move colours to their own class
        self.background_colour = (255, 255, 255)
        self.line_colour = (0, 0, 255)
        self.width = width
        self.height = height

        self.screen_width = self.square_size * self.width + self.margin * 2
        self.screen_height = self.square_size * self.height + self.margin * 2

        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))

    def draw_grid(self):
        for tik in range(0, self.width + 1):
            vstart = (self.margin + (tik * self.square_size), self.margin)
            vend = (self.margin + (tik * self.square_size), self.screen_height - self.margin)
            pygame.draw.line(self.display, self.line_colour, vstart, vend)

        for tik in range(0, self.height + 1):
            hstart = (self.margin, self.margin + (tik * self.square_size))
            hend = (self.screen_width - self.margin, self.margin + (tik * self.square_size))
            pygame.draw.line(self.display, self.line_colour, hstart, hend)

    def draw_background(self):
        self.display.fill(self.background_colour)
        self.draw_grid()
