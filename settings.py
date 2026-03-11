class Settings:
    """Control the overall settings for the game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 5
        self.lives = 3

        # Bullet Settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 50

        # Alien Settings
        self.alien_speed = 1
        self.fleet_drop_speed = 30
        self.fleet_drop_direction = 1       # Using 1 here for right and -1 for left
