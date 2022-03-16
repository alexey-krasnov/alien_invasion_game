import pygame.font


class Scoreboard:
    """Class for showing game information"""

    def __init__(self, ai):
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

    def prep_score(self):
        """Transform current score to image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Show score at the right upper corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Show score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
