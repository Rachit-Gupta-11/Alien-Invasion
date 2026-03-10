import pygame
class Ship:
    """A class to manage the ship"""

    def __init__(self,ai_game):
        # Initializes the ship and its start position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get the rectange for it
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each ship at the midbottom 
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

    def _update(self):
        """Update ships position based on movement flag"""  
        if self.moving_right:
            self.rect.x += 5
        elif self.moving_left:
            self.rect.x -= 5

    def blitme(self):
        # Draw the ship at curr location
        self.screen.blit(self.image,self.rect)
    
