# monster.py

import pygame

class Monster:
    def __init__(self):
        self.x = 0
        self.y = 100
        self.speed = 2

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 30, 30))

    def update(self):
        self.x += self.speed
