import pygame

class Stats:
    """Track the stats of the game"""

    def __init__(self,game):
        self.settings = game.settings
        self.reset()

    def reset(self):
        self.ships_left = self.settings.lives
        
     