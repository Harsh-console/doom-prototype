import pygame
from constants import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
    def start_game(self):
        pass
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    def draw(self):
        self.screen.fill(BLACK)
    def update(self):
        self.clock.tick(FPS)
        pygame.display.set_caption(f'FPS : {self.clock.get_fps():.1f}')
        pygame.display.update()
    def run(self):
        self.start_game()
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()