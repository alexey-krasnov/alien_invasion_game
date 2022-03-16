import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class for one alien"""
    def __init__(self, ai):
        """Initialize the alien and sets its initial position"""
        super().__init__()
        self.screen = ai.screen

        # Loading an Alien Image and Assigning an Attribute rect
        self.image = pygame.image.load('../images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the Alien's Accurate Horizontal Position
        self.x = float(self.rect.x)

        self.settings = ai.settings

    def check_edges(self):
        """Return True if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move aliens right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
