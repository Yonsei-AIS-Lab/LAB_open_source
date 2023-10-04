# obstacle.py

import pygame

class Obstacle:
    def __init__(self, x, speed):
        self.x = x
        self.y = 0
        self.speed = speed
        self.color = (0, 0, 255)
        self.width = 30
        self.height = 30

    def collide(self, player):
        return pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
            pygame.Rect(player.x - player.radius, player.y - player.radius, player.radius * 2, player.radius * 2)
        )

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
