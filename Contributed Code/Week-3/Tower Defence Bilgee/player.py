import pygame
from tower import Tower

class Player:
    def __init__(self):
        # 플레이어 초기화
        self.position = pygame.Vector2(400, 500)
        self.velocity = pygame.Vector2(0, 0)
        self.player_health = 100
        self.speed = 500
        self.towers = []

    def move(self, direction):
        # 플레이어 이동 설정
        self.velocity = direction * self.speed

    def update(self, dt, monsters):
        # 플레이어 업데이트
        self.position += self.velocity * dt

    def place_tower(self):
        # 타워 배치
        if len(self.towers) < 3:
            self.towers.append(Tower(*self.position))

    def reset_towers(self):
        # 타워 초기화
        print("리셋")
        print(self.towers)
        self.towers = []
        print(self.towers)

    def draw(self, screen):
        # 플레이어 그리기
        pygame.draw.rect(screen, (0, 128, 255), (*self.position, 30, 30))
        health_bar_width = 30
        health_percentage = max(self.player_health / 100, 0)
        health_bar_fill_width = int(health_percentage * health_bar_width)
        health_bar_rect = pygame.Rect(self.position.x, self.position.y - 10, health_bar_fill_width, 5)
        pygame.draw.rect(screen, (0, 255, 0), health_bar_rect)
