import sys
import pygame

class AlienInvasion:
    """Class to manage game assets and behavior """

    def __init__(self):
        """Initialze the game and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
        self.bg_color = (230, 230, 230)
        self.screen.fill(self.bg_color)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run the game
    alienInvasion = AlienInvasion()
    alienInvasion.run_game()