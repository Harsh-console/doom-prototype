from typing import Any
import pygame as pg
from settings import *

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, 1],
]

class MAP:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(self.mini_map[j]):
                if value:
                    self.world_map[(i,j)] = value
    
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (int(pos[0]*(WIDTH / len(mini_map[0])), int(pos[1] * ( HEIGHT / len(mini_map)))), int(WIDTH / len(mini_map[0]))), int(( HEIGHT / len(mini_map))), 2)
        for pos in self.world_map]
