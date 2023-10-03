import random
from monster import Monster
import pygame

class Wave:
    def __init__(self, wave_number, game):
        # 웨이브 초기화
        self.wave_number = wave_number
        self.monster_count = 5 + wave_number
        self.spawn_interval = 20
        self.spawn_timer = 0
        self.game = game
        self.spawned = 0

    def update(self, monsters, player):
        # 웨이브 업데이트
        if self.spawned < self.monster_count:
            self.spawn_timer += 1
            if self.spawn_timer >= self.spawn_interval:
                self.spawn_monster(monsters)
                self.spawn_timer = 0
                self.spawned += 1
        else:
            if len(monsters) == 0:
                self.wave_number += 1
                self.spawned = 0
                player.towers = []

    def spawn_monster(self, monsters):
        # 몬스터 생성
        position = pygame.Vector2(0, random.randint(100, 500))
        monsters.append(Monster(monsters, position, self.game))
