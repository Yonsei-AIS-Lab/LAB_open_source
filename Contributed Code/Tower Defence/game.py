# game.py

import pygame
from player import Player
from monster import Monster

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tower Defense Game")
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.monsters = [Monster() for _ in range(5)]  # 5마리의 몬스터 생성

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def draw(self):
        self.screen.fill((0, 0, 0))  # 배경을 검은색으로 지정
        self.player.draw(self.screen)  # 플레이어 그리기
        for monster in self.monsters:
            monster.draw(self.screen)  # 몬스터들 그리기

    def update(self):
        self.player.update(self.monsters)
        for monster in self.monsters:
            monster.update()

        # 플레이어와 몬스터 간의 충돌 체크 및 게임 종료 조건 확인

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.place_tower()

    def quit(self):
        pygame.quit()
