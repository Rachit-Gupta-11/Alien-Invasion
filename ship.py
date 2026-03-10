import pygame
class Ship:
    """A class to manage the ship"""

    def __init__(self,ai_game):
        # Initializes the ship and its start position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get the rectange for it
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each ship at the midbottom 
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for ships horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def _update(self):
        """Update ships position based on movement flag"""  
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # if both the keys are pressed at the same time no movement
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        # Keep an attribute in self for its current position and in update set self.rect.x to self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # Draw the ship at curr location
        self.screen.blit(self.image,self.rect)
    
