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
        
        self.monsters = [monster for monster in self.monsters if monster.health > 0]  # 죽은 몬스터 제거
        self.check_collisions_and_game_over() # 충돌 체크 및 게임 종료 조건 확인

        # 플레이어와 몬스터 간의 충돌 체크 및 게임 종료 조건 확인


    def check_collisions_and_game_over(self):
        # 플레이어와 몬스터 간의 충돌 체크 로직
        for monster in self.monsters:
            distance = ((self.player.x - monster.x) ** 2 + (self.player.y - monster.y) ** 2) ** 0.5
            if distance < 30:
                self.game_over()
    
    def game_over(self):
        # 게임 종료 조건 확인 및 처리 로직
        print("Game Over!")  # 간단하게 콘솔에 출력하는 예
        pygame.quit()
    
    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.place_tower()

    def quit(self):
        pygame.quit()
