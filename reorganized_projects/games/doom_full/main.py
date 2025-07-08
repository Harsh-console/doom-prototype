import pygame
import sys
from settings import *
from map import *
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game() 

    def new_game(self):
        self.map = MAP(self)

    def update(self):
        pygame.display.update()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'FPS : {self.clock.get_fps():.1f}')
    
    def draw(self):
        self.screen.fill('Black')
        self.map.draw()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
    