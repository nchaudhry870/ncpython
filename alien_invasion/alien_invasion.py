import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class to manage game assets and behavior """

    def __init__(self):
        """Initialze the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            

            
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keyboard and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run the game
    alienInvasion = AlienInvasion()
    alienInvasion.run_game()