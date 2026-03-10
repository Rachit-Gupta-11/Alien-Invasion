import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien



class AlienInvasion:
    """Overall Class to manage behaviour and game assets"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200,800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)      # get the ship element
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
    
    def _create_fleet(self):
        """Create a fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        curr_y = alien_height
        curr_x = alien_width
        while curr_y < (self.settings.screen_height - 3*alien_height):
            while curr_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(curr_x,curr_y)
                curr_x += 2*alien_width
            
            curr_x = alien_width
            curr_y += 2*alien_height
        
    def _create_alien(self, pos, posy):
        """Create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = pos
        new_alien.rect.x = pos
        new_alien.rect.y = posy
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Responds when aliens reached the end of the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_drop_direction*=-1


    def run_game(self):
        while True:
            self._check_events()
            self.ship._update()
            self._update_bullets()
            self._update_aliens()

            self._update_screen()
            self.clock.tick(60)     # For 60 FPS
        

    def _update_aliens(self):
        """Update the aliens in the list"""   
        self._check_fleet_edges()
        self.aliens.update()

    def _update_bullets(self):
        """Update the bullets and remove them when out of screen"""
        # Update position of bullet
        self.bullets.update()

        # Check for going out of screen
        for bul in self.bullets.copy():
            if bul.rect.bottom <= 0:
                self.bullets.remove(bul)
        # print(len(self.bullets))


    def _check_events(self):
        """Respond to keypress and mouse clicks"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Repond to Keypresses"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_q:
            sys.exit()
        
    def _fire_bullet(self):
        """Create a bullet and add it to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self)) 

    def _check_keyup_events(self,event):
        """Respond to keyReleases"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False

    def _update_screen(self):
        """ Update images and graphics on the screen """
        
        # Redraw the screen through each pass of the loop
        self.screen.fill(self.settings.bg_color)
        for bul in self.bullets:
            bul.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)


        # Make the recently drawn screen visible
        pygame.display.flip()


    
if __name__=='__main__':
    """Make a game instance and run the game"""

    ai = AlienInvasion()
    ai.run_game()
