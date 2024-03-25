import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Class to manage game assets and behavior """

    def __init__(self):
        """Initialze the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.screen.fill(self.settings.bg_color)
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick()

if __name__ == '__main__':
    #make a game instance and run the game
    alienInvasion = AlienInvasion()
    alienInvasion.run_game()