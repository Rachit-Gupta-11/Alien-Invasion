import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall Class to manage behaviour and game assets"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)      # get the ship element


    def run_game(self):
        while True:
            self._check_events()
            self.ship._update()
            self._update_screen()
            self.clock.tick(60)     # For 60 FPS
        
    def _check_events(self):
        """Respond to keypress and mouse clicks"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Else move to left
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                self.ship.moving_left = False
                self.ship.moving_right = False


    def _update_screen(self):
        """Update images and graphics on the screen"""
        
        # Redraw the screen through each pass of the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the recently drawn screen visible
        pygame.display.flip()


    
if __name__=='__main__':
    """Make a game instance and run the game"""
    ai = AlienInvasion()
    ai.run_game()

