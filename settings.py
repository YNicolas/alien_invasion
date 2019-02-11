#!/usr/bin/python3 
class Settings:
    def __init__(self):
        # Initialize Settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
