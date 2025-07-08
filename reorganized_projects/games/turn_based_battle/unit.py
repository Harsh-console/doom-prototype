from constants import *
import pygame

class Character():
    def __init__(self, game, color, init_pos, health, max_health):
        self.game = game
        self.color = color
        self.init_pos = init_pos
        self.surface = pygame.Surface((TILE,TILE))
        self.rect = self.surface.get_rect(topleft = self.init_pos)
        chars_.append(self)
        self.surface.fill(self.color)
        self.health = health
        self.max_health = max_health
