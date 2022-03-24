import pygame


class Ship:
    """Class for managing ship"""
    def __init__(self, ai):
        """Initializes the ship and set its initial position"""
        self.screen = ai.screen
        self.settings = ai.settings  # Create a settings attribute to use in update
        self.screen_rect = ai.screen.get_rect()

        # Loads a ship image and get a rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Each new ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Store the real coordinate of the ship's center in a new attribute self.x
        self.x = float(self.rect.x)
        # Move right and left flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the flag"""
        # The x attribute of the ship object is updated, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at the current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Place s ship in the midbottom"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
