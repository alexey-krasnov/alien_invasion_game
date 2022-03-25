class Settings:
    """Class to store all Alien Invasion game settings"""

    def __init__(self):
        """Initialize static game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_left = 3

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # Dark gray bullets
        self.bullet_allowed = 5

        # Aliens settings
        self.fleet_drop_speed = 10

        # Game acceleration rate
        self.speedup_scale = 1.1

        # The growth rate of the value of aliens
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings changing during game"""
        self.ship_speed = 1.6
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction = 1 is moving right, -1 is moving left
        self.fleet_direction = 1

        # Count of scores
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings amd aliens cost"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
