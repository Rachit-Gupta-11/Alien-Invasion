import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self,ai_game):
        """Create a bullet object at the ships curr position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect:
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullets positions:
        self.y = float(self.rect.y)
        # self.x = float(self.rect.x)

    def update(self):
        """Move the bullets up the screen """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Deaw the bullets on the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
