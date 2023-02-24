class Settings:
    # A class to store all settings for Alien Invasion

    def __init__(self):
        # Initialize the game's static settings

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 1

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 20

        # How quickly the game speeds up
        self.speedup_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game
        self.ship_speed = 10
        self.bullet_speed = 5.0
        self.alien_speed = 2.0

        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 10

    def increase_speed(self):
        # Increase speed settings
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
