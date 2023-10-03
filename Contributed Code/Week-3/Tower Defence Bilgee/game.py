import pygame
from player import Player
from monster import Monster
import random
import pygame.font as pf
from wave import Wave

class Game:
    def __init__(self):
        # Pygame 초기화 및 화면 생성
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("타워 디펜스 게임")
        self.clock = pygame.time.Clock()
        
        # 벽 초기화
        self.wall_rect = pygame.Rect(770, 0, 30, 600)
        self.collided_with_wall = False

        # 플레이어, 웨이브, 몬스터, 타워 초기화
        self.player = Player()
        self.wave = Wave(1, self)
        self.monsters = []
        self.towers = self.player.towers

        # 폰트 초기화
        self.font = pf.Font(None, 36)

        # 게임 오버 상태 초기화
        self.game_over = False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # 이벤트 처리, 게임 상태 업데이트, 화면 그리기
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def draw(self):
        if not self.game_over:
            # 게임이 끝나지 않았을 때 화면 그리기
            self.screen.fill((0, 0, 0)) 
            self.player.draw(self.screen) 
            self.display_controls()
            for monster in self.monsters:
                monster.draw(self.screen)
            for tower in self.player.towers:
                tower.draw(self.screen)
        else:
            # 게임 오버 화면 그리기
            self.screen.fill((0, 0, 0))
            self.display_controls()

    def update(self):
        if not self.game_over:
            dt = self.clock.tick(60) / 1000.0 
            self.player.update(dt, self.monsters)
            for monster in self.monsters:
                monster.update()
            
            for tower in self.player.towers:
                tower.update(self.monsters, self.player)

            self.wave.update(self.monsters, self.player)
        

    def handle_events(self):
        # 키 입력 처리
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)
        if keys[pygame.K_LEFT]:
            direction.x = -1
        if keys[pygame.K_RIGHT]:
            direction.x = 1
        if keys[pygame.K_UP]:
            direction.y = -1
        if keys[pygame.K_DOWN]:
            direction.y = 1
        if keys[pygame.K_SPACE]:
            if not self.space_pressed:
                self.space_pressed = True
                self.player.place_tower()
        else:
            self.space_pressed = False
            self.player.move(direction)

    def display_controls(self):
        if self.game_over == True:
            text = "Game Over"
        elif self.wave.wave_number == 1:
            text = "Arrow keys to move, Space to place towers!"
        else:
            text = f"Wave {self.wave.wave_number - 1}"
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 30))

        self.screen.blit(text_surface, text_rect)

    def reached_wall(self, monster):
        # 몬스터가 벽에 도달했을 때의 처리
        self.monsters.remove(monster)
        self.player.player_health -= 10

        if self.player.player_health <= 0:
            self.game_over = True

    def quit(self):
        # 게임 종료
        pygame.quit()
