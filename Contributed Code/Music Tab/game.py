# game.py

import pygame
import os
from player import Player
from obstacle import Obstacle
from music import Music
import random  # random 모듈을 가져옴

class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Rhythm Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player()
        self.obstacles = []
        self.music = Music("./Original Code/Music Tab/background_music.mp3")

    def run(self):
        self.music.play()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.tap()

    def spawn_obstacles(self):
        # 음악에 맞게 장애물 생성
        # 예시로 무작위로 장애물을 생성합니다.
        if random.randint(0, 100) < 5:  # 임의로 선택한 확률
            x = random.randint(0, self.screen_width - 30)  # 화면 내 랜덤한 위치에 생성
            speed = 5  # 장애물의 속도
            self.obstacles.append(Obstacle(x, speed))

    def update(self):
        self.obstacles = [obstacle for obstacle in self.obstacles if not obstacle.collide(self.player)]
        self.player.update()
        self.spawn_obstacles()
        for obstacle in self.obstacles:
            obstacle.move()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
