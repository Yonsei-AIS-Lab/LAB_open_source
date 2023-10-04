# monster.py

import pygame

class Monster:
    def __init__(self):
        self.x = 0
        self.y = 100
        self.speed = 2
        self.health = 100 # 몬스터의 체력

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()
            
    def die(self):
        print("Monster died!")
        #실제 몬스터 객체는 삭제되지 않고, Game 클래스에서 몬스터 목록을 업데이트할 때 삭제됨

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 30, 30))

    def update(self):
        self.x += self.speed
