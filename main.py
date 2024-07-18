#import pygame module, import GUI Screen, Import Player 
import pygame
from Settings import *
from Player import *
import Player
from Marketplace import *
from Level import level
import sys

#Initialize Pygame
class Game:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("Support Desk")
        self.clock = pygame.time.Clock()

        self.Level = level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill("white")
            self.Level.run()
            pygame.display.update()
            self.clock.tick(SCREEN_FPS)

if __name__ == '__main__':
    game = Game()
    game.run()

    

    

