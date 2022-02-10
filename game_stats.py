class GameStats():
    """Check statistics for the game Alien Invasion"""

    def __init__(self, ai):
        """Initialize statisics"""
        self.settings = ai.settings
        self.reset_stats()
        # The game starts at the inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize stats, changing during the game"""
        self.ships_left = self.settings.ship_left
        self.score = 0
        