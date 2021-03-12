class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2
        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (240,240,240)
        self.bullet_allowed = 3
        #Alien settings
        self.alien_speed = 0.3
        self.fleet_drop_speed = 8
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
