import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for managing projectiles fired by a ship"""
    def __init__(self, ai):
        """Create an object with a projectile at the ship's current position"""
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.color = self.settings.bullet_color

        # Creating a bullet at position (0,0) and assign the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai.ship.rect.midtop  # The bullet's midtop attribute is set to the value of the ship's midtop

        # Bullet position is stored in real format
        self.y = float(self.rect.y)  # The top edge of the bullet is aligned with the top edge of the ship rectangle

    def update(self):
        """Move the projectile up the screen"""
        # updating the position of the projectile in real format
        self.y -= self.settings.bullet_speed
        # Rectangle Position Update
        self.rect.y = self.y

    def draw_bullet(self):
        """Displays bullets on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
