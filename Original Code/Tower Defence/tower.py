# tower.py

import pygame

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attack_range = 100
        self.damage = 10
        self.target = None

    def find_target(self, monsters):
        for monster in monsters:
            distance = ((self.x - monster.x) ** 2 + (self.y - monster.y) ** 2) ** 0.5
            if distance <= self.attack_range:
                self.target = monster
                break
        else:
            self.target = None

    def attack(self):
        if self.target:
            self.target.take_damage(self.damage)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, 30, 30))

    def update(self, monsters):
        self.find_target(monsters)
        self.attack()
