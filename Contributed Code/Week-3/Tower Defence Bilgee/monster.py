import pygame

class Monster:
    def __init__(self, monsters, position, game):
        # 몬스터의 초기화
        self.position = position
        self.health = 100
        self.speed = 2
        self.monsters = monsters
        self.game = game
        self.list = []

    def draw(self, screen):
        # 몬스터를 화면에 그림
        pygame.draw.rect(screen, (255, 0, 0), (*self.position, 30, 30))
        health_bar_width = 30 
        health_percentage = max(self.health / 100, 0)
        health_bar_fill_width = int(health_percentage * health_bar_width)
        health_bar_rect = pygame.Rect(self.position.x, self.position.y - 10, health_bar_fill_width, 5)
        pygame.draw.rect(screen, (0, 255, 0), health_bar_rect)


    def update(self):
        # 몬스터의 업데이트
        self.position.x += self.speed

        if self.position.x > 770:
            # 몬스터가 벽에 도달했을 때의 처리
            self.game.reached_wall(self)
    
    def take_damage(self, damage):
        # 몬스터가 피해를 받을 때의 처리
        self.health -= damage
        if self.health <= 0:
            if len(self.monsters) != 0:
                self.monsters.remove(self)
