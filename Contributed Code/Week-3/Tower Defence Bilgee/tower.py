import pygame

class Tower:
    def __init__(self, x, y):
        # 타워 초기화
        self.position = pygame.Vector2(x, y)
        self.attack_range = 100
        self.damage = 10
        self.target = None
        self.cooldown = 100
        self.last_attack = pygame.time.get_ticks()

    def find_target(self, monsters):
        # 공격 대상 찾기
        now = pygame.time.get_ticks()
        for monster in monsters:
            distance = ((self.position.x - monster.position.x) ** 2 + (self.position.y - monster.position.y) ** 2) ** 0.5
            if distance <= self.attack_range:
                self.target = monster
                break
            else:
                self.target = None

    def attack(self, player):
        # 공격 실행
        now = pygame.time.get_ticks()
        if self.target and now - self.last_attack >= self.cooldown and self in player.towers:
            self.target.take_damage(self.damage)
            self.last_attack = now

    def draw(self, screen):
        # 타워 그리기
        pygame.draw.rect(screen, (255, 255, 0), (*self.position, 30, 30))

    def update(self, monsters, player):
        # 타워 업데이트
        self.find_target(monsters)
        self.attack(player)
