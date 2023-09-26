# player.py

import pygame
from tower import Tower

class Player:
    def __init__(self):
        self.x = 400
        self.y = 500
        self.towers = []

    def place_tower(self):
        if len(self.towers) < 3:
            self.towers.append(Tower(self.x, self.y))

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 128, 255), (self.x, self.y, 30, 30))

    def update(self, monsters):
        for tower in self.towers:
            tower.update(monsters)
