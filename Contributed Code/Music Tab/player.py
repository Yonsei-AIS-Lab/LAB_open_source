# player.py

import pygame

class Player:
    def __init__(self):
        self.x = 400
        self.y = 500
        self.radius = 20
        self.color = (255, 0, 0)
        self.score = 0

    def tap(self):
        # 탭 이벤트 처리 및 점수 증가
        self.score += 1

    def update(self):
        # 플레이어 상태 업데이트
        self.move(800)  # 예시: 플레이어 움직임 업데이트

    def move(self, screen_width):
        # 플레이어의 움직임 업데이트 로직을 추가
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x - self.radius > 0:
            self.x -= 5
        if keys[pygame.K_RIGHT] and self.x + self.radius < screen_width:
            self.x += 5


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
