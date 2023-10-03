"""
텍스트 기반 던전 크롤러 게임을 만들려고 합니다. 
이 게임에는 플레이어와 몬스터가 등장하며, 플레이어는 몬스터를 공격하여 처치하거나 회복하여 생존해야 합니다. 
아래는 게임을 구현하기 위한 파이썬 코드의 일부입니다.
"""

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = random.randint(10, 20) # 수정
        self.inventory = []

    def attack(self):
        return self.power #수정

    def heal(self):
        self.health += random.randint(10, 20)

    def take_damage(self, damage):
        self.health -= damage

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 100)
        self.attack_damage = random.randint(5, 15)

    #def attack(self): 굳이 필요없음 삭제 
    #    return self.attack_damage
    
    def take_damage(self, damgage): #함수 추가
        self.health -= damgage

def main():
    player_name = input("플레이어 이름을 입력하세요: ")
    player = Player(player_name)

    monsters = [Monster("고블린"), Monster("드래곤"), Monster("스켈레톤")]

    print(f"{player.name}님, 던전 크롤러에 오신 것을 환영합니다!")
    
    while player.health > 0:
        print(f'\n체력: {player.health}') #코드추가
        print(f'공격력: {player.power}') #코드추가
        print(f'인벤토리: {player.inventory}') #코드추가 
        command = input("어떤 행동을 하시겠습니까? (공격/회복/나가기): ").lower()

        if command == "나가기":
            #print("게임을 종료합니다.") 필요없는 메시지 삭제
            break
        elif command == "공격":
            monster = random.choice(monsters)
            print(f"\n{player.name}님이 {monster.name}을(를) 공격합니다!") #줄바꿈 추가
            damage = player.attack()
            monster.take_damage(damage)
            print(f"{monster.name}에게 {damage}의 데미지를 입혔습니다.")
            print(f"{monster.name}의 체력: {monster.health}") #코드추가
            if monster.health <= 0:
                print(f"{monster.name}을(를) 처치하였습니다!")
                print(f"'{monster.name}의 아이템'을 습득하였습니다.") #코드추가
                player.inventory.append(f"{monster.name}의 아이템")
            else: # 몬스터의 반격 추가
                player.take_damage(monster.attack_damage)
                print(f'\n{monster.name}이 공격합니다!')
                print(f"{player.name}에게 {monster.attack_damage}의 데미지를 입혔습니다.")
                print(f"{player.name}의 체력: {player.health}") #코드추가
                if player.health < 1:
                    print(f'{player.name}님이 죽었습니다! ', end='')
                    break
        elif command == "회복":
            player.heal()
            print(f"\n{player.name}님이 회복하였습니다. 현재 체력: {player.health}") #줄바꿈 추가

    print("게임이 종료되었습니다.\n") #줄바꿈 추가
    if len(player.inventory) == 0: #코드 추가 처지 안하고 나가면 패배
        print(f"몬스터를 처치 실패했습니다. {player.name}님의 패배!")
    else:
        print(f"{player.name}님의 승리! 획득한 아이템: {', '.join(player.inventory)}")

if __name__ == "__main__":
    main()
