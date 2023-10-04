"""
텍스트 기반 던전 크롤러 게임을 만들려고 합니다. 
이 게임에는 플레이어와 몬스터가 등장하며, 플레이어는 몬스터를 공격하여 처치하거나 회복하여 생존해야 합니다. 
아래는 게임을 구현하기 위한 파이썬 코드의 일부입니다.
"""

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.inventory = []

    def attack(self):
        return random.randint(10, 20)

    def heal(self):
        self.health += random.randint(10, 20)

    def take_damage(self, damage):
        self.health -= damage

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 100)
        self.attack_damage = random.randint(5, 15)

    def attack(self):
        return self.attack_damage
    
    def take_damage(self, damage):
        self.health -= damage

def main():
    player_name = input("플레이어 이름을 입력하세요: ")
    player = Player(player_name)

    monsters = [Monster("고블린"), Monster("드래곤"), Monster("스켈레톤")]

    print(f"{player.name}님, 던전 크롤러에 오신 것을 환영합니다!")

    while player.health > 0:
        command = input("어떤 행동을 하시겠습니까? (공격/회복/나가기): ").lower()

        if command == "나가기":
            print("게임을 종료합니다.")
            exit(0)
        elif command == "공격":
            monster = random.choice(monsters)
            
            print(f"{player.name}님이 {monster.name}을(를) 공격합니다!")
            damage = player.attack()
            monster.take_damage(damage)
            print(f"{monster.name}에게 {damage}의 데미지를 입혔습니다.")
            if monster.health <= 0:
                monster.health = 0
                print(f"{monster.name}의 체력: {monster.health}\n")
                print(f"{monster.name}을(를) 처치하였습니다!")
                player.inventory.append(f"{monster.name}의 아이템")
                print(f"{player.name}이 {monster.name}의 아이템을 획득하였습니다!")
                monsters.remove(monster)
                continue
            else:
                print(f"{monster.name}의 체력: {monster.health}\n")

            print(f"{monster.name}이 {player.name}님을 공격합니다!")
            damaged = player.attack()
            player.take_damage(damaged)
            print(f"{player.name}님이 {damaged}의 데미지를 입었습니다.")
            if player.health <= 0:
                player.health = 0
                print(f"{player.name}의 체력: {player.health}\n")
                print(f"{player.name}님이 사망하였습니다.")
                print("게임을 종료합니다.")
                print(f"{player.name}님의 패배... 획득한 아이템: {', '.join(player.inventory)}")
                exit(0)
            else:
                print(f"{player.name}의 체력: {player.health}\n")

        elif command == "회복":
            player.heal()
            print(f"{player.name}님이 회복하였습니다. 현재 체력: {player.health}")

    print("게임이 종료되었습니다.")
    print(f"{player.name}님의 승리! 획득한 아이템: {', '.join(player.inventory)}")

if __name__ == "__main__":
    main()