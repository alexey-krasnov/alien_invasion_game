import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """Class for showing game information"""
    def __init__(self, ai):
        self.ai = ai
        """Initialize attributes scoring """
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai.settings
        self.stats = ai.stats

        # font settings for score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # preparation  of initial image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Transform current score to image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f'{rounded_score:,}'
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Show score at the right upper corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Show score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def prep_high_score(self):
        """Transform record score to image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f'{high_score:,}'
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.ai.settings.bg_color)

        # The record is centered on the top side
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def check_high_score(self):
        """Checks if a new record has appeared"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def prep_level(self):
        """Converts level to a graphic"""
        level_Str = str(self.stats.level)
        self.level_image = self.font.render(level_Str, True,
             self.text_color, self.settings.bg_color)

        #The level is displayed under the current account
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_ships(self):
        """Reports the number of remaining ships"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
