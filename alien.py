import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Contains the code for the alien objects"""

    def __init__(self,ai_game):
        """initialize the alien class and set the starting points"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Each new alien will start at the top left
        self.rect.x  = self.rect.width
        self.rect.y = self.rect.height

        #store the aliens exact horizontal location
        self.x = float(self.rect.x)

    

    def update(self):
        """Move the alien""" 
        self.x += self.settings.alien_speed * self.settings.fleet_drop_direction
        self.rect.x = self.x

    def check_edges(self):
        """Check if the alien has hit the edge of the boundry"""
        screen_rect = self.screen.get_rect()
        check1 = screen_rect.left >= self.rect.left
        check2 = screen_rect.right<= self.rect.right
        return check1 or check2
    
    
