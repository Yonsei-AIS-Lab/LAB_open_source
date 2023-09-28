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
        self.defense = 0
        self.attack_damage = 100
        self.desc = "당신입니다."
        self.inventory = []

    def heal(self):
        self.health += random.randint(10, 20)

    def take_damage(self, damage):
        damage_taken  = damage - self.defense
        if (damage_taken > 0):
            self.health -= damage

class Monster:
    def __init__(self, name, desc, items):
        self.name = name
        self.health = random.randint(50, 100)
        self.attack_damage = random.randint(5, 15)
        self.defense = 0
        self.desc = desc
        self.inventory = items

    def attack(self):
        return self.attack_damage
    
    def take_damage(self, damage):
        self.health -= damage

class Item:
    def __init__(self, name, desc, effect, amount):
        self.name = name
        self.desc = desc
        self.effect = effect
        self.amount = amount
    
    def use(self, player):
        self.effect(self, player)
    
    def inc_attack_damage(self, player):
        player.attack_damage += self.amount
    
    def inc_defense(self, player):
        player.defense += self.amount

    def do_nothing(self, player):
        player.desc = "고블린의 눈을 가지고 있는 당신입니다."

def main():
    player_name = input("플레이어 이름을 입력하세요: ")
    player = Player(player_name)

    s_sword = Item("스켈레톤의 검", "공격력 +10", Item.inc_attack_damage, 10)
    d_skin = Item("용의 비늘", "방어력 +5", Item.inc_defense, 5)
    g_eye = Item("고블린의 눈", "눈입니다.", Item.do_nothing, 0)

    monsters = [Monster("고블린", "못 생겼습니다.", [g_eye]),
                Monster("드래곤", "용이기에 너무 작습니다.", [d_skin]), 
                Monster("스켈레톤", "날씬합니다.", [s_sword])]

    print(f"{player.name}님, 던전 크롤러에 오신 것을 환영합니다!")

    while player.health > 0 and len(monsters) > 0:
        print("\n")
        monster_names = []
        for monster in monsters:
            print('{', monster.name ,' : ', monster.health, '} ', end='')
            monster_names.append(monster.name)
        print("\n\n\n")
        print('{', player.name , " : ", player.health,'}', '\n')
        
        command = input("어떤 행동을 하시겠습니까? (공격/회복/보기/아이템/나가기): ").lower()

        if command == "나가기":
            print("게임을 종료합니다.")
            break
        elif command == "보기":
            ## 몬스터 선택하기
            found = False
            while found == False:
                monster_name = input(f"누구를 보겠습니까? ({'/'.join(monster_names)}/{player.name}): ")
                if (monster_name == player.name):
                    inspected_monster = player
                    found = True
                else:
                    for monster in monsters:
                        if monster.name == monster_name:
                            found = True
                            inspected_monster = monster
                    if found == False:
                        print(f"{monster_name}이(가) 존재하지 않습니다. 다시 시도해 주세요.")
                        continue
                
                print(f"\n이름: {inspected_monster.name}")
                print(f"설명: {inspected_monster.desc}")
                print(f"체력: {inspected_monster.health}")
                print(f"공격력: {inspected_monster.attack_damage}")
                print(f"아이템들: {', '.join(item.name for item in inspected_monster.inventory)}")
                print(f"방어력: {inspected_monster.defense}")
            
        ##아이템 사용
        elif command == "아이템":
            if(player.inventory == []):
                print("\n아이템이 없습니다.")
            else:
                found = False
                while found == False:
                    print("\n어떤 아이템을 사용하겠습니까?\n")
                    for item in player.inventory:
                        print(item.name, ' : ', item.desc)
                    
                    selected_item = input("\n사용하실 아이템의 이름을 입력하세요: ")
                    for item in player.inventory:
                        if selected_item == item.name:
                            found = True
                            item.use(player)
                            print(f"{item.name}을 사용했습니다!")
                            player.inventory.remove(item)
                        else:
                            print("선택하신 아이템이 없습니다. 다시 시도해 주세요.")

        elif command == "공격":
            ## 몬스터 선택하기
            found = False
            while found == False:
                monster_name = input(f"누구를 공격하겠습니까? ({'/'.join(monster_names)}): ")
                for monster in monsters:
                    if monster.name == monster_name:
                        found = True
                        defending_monster = monster
                if found == False:
                    print(f"{monster_name}이(가) 존재하지 않습니다. 다시 시도해 주세요.")

            ##몬스터 공격하기
            print(f"\n{player.name}님이 {defending_monster.name}을(를) 공격합니다!")
            damage = player.attack_damage
            defending_monster.take_damage(damage)
            print(f"{defending_monster.name}에게 {damage}의 데미지를 입혔습니다.")
            if defending_monster.health <= 0:
                print(f"{defending_monster.name}을(를) 처치하였습니다!")
                monsters.remove(defending_monster)
                for item in defending_monster.inventory:
                    player.inventory.append(item)

        elif command == "회복":
            player.heal()
            print(f"{player.name}님이 회복하였습니다. 현재 체력: {player.health}")
        else:
            print("잘못 입력하셨습니다.")
            continue
        
        ##공격 당하기
        if command == "보기" or command == "아이템" or len(monsters) == 0:
            continue
        else:
            attacking_monster = random.choice(monsters)

            damage = attacking_monster.attack()
            player.take_damage(damage)
            
            damage_taken = damage - player.defense
            if (damage_taken < 0):
                damage_taken == 0
            print(f"{attacking_monster.name}이(가) {player.name}에게 {damage}의 데미지를 입혔습니다.")
    print("게임이 종료되었습니다.")
    if len(monsters) == 0 :
        print(f"{player.name}님의 승리!")
    else:
        print(f"몬스터들이 이겼습니다.")

if __name__ == "__main__":
    main()

