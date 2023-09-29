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
        self.inventory = []

    # 플레이어의 공격 메서드. 랜덤한 데미지를 반환합니다.
    def attack(self):
        return random.randint(10, 20)

    # 플레이어의 회복 메서드. 랜덤한 체력을 회복합니다.
    def heal(self):
        self.health += random.randint(10, 20)

    # 플레이어가 데미지를 받는 메서드. 입력된 데미지만큼 체력을 감소시킵니다.
    def take_damage(self, damage):
        self.health -= damage

class Monster:
    def __init__(self, name, item):   # 몬스터 클래스 초기화 함수에 아이템 파라미터 추가
        self.name = name
        self.item = item              # 몬스터 아이템 설정 
        self.health = random.randint(50, 100)
        self.attack_damage = random.randint(5, 15)

    # 몬스터의 공격 메서드. 몬스터의 공격력을 반환합니다.
    def attack(self):
        return self.attack_damage

    # 몬스터가 데미지를 받는 메서드. 입력된 데미지만큼 체력을 감소시킵니다.
    def take_damage(self, damage):   
         self.health -= damage
         if self.health < 0: 
             self.health = 0 

def print_health_status(player: Player , monsters: list):   # 체력 상태 출력 
     print(f"\n{player.name}님의 현재 체력: {player.health}")
     for monster in monsters:
         if monster.health > 0:
             print(f"몬스터 {monster.name}({monster.item}) 의 남은 체력: {monster.health}")

def main():
    
   player_name = input("플레이어 이름을 입력하세요: ")
   player = Player(player_name)
   
   monsters = [Monster("고블린", "고블린의 칼"), Monster("드래곤", "드래곤의 비늘"), Monster("스켈레톤", "스켈레톤의 해골")]  
   
   print(f"\n==== 게임 시작 ====")
   print_health_status(player, monsters)  # 게임 시작 시 체력 상태 출력
   
   while player.health > 0:
       command = input("\n[명령 선택]\n1)공격\n2)회복\n3)나가기\n명령어를 입력하세요: ")
    
       if command == "나가기":
            print("\n==== 게임 종료 ====")
            
            if len(player.inventory) == 0:
                print(f"{player.name}님이 획득한 아이템이 없습니다.") 
            else:
                print(f"{player.name}님의 승리! 획득한 아이템: {', '.join(player.inventory)}")
            
            return 
       
       elif command == "공격":
            alive_monsters = [monster for monster in monsters if monster.health > 0] 
            
            if not alive_monsters:
                print("모든 몬스터를 처치하셨습니다!")
                break
            
            monster_to_attack= random.choice(alive_monsters)
            
            damage_to_monster= player.attack()
            
            monster_to_attack.take_damage(damage_to_monster)
           
            if monster_to_attack.health <= 0:
                print(f"\n{monster_to_attack.name}을(를) 처치하였습니다!")
                player.inventory.append(monster_to_attack.item) # 몬스터가 가진 아이템을 플레이어 인벤토리에 추가
                
                alive_monsters_after_attack = [monster for monster in monsters if monster.health > 0]
                
                if not alive_monsters_after_attack: 
                    print("모든 몬스터를 처치하셨습니다! 게임에서 승리하셨습니다.")
                    return
            

            
            damage_from_monster = monster_to_attack.attack()
            player.take_damage(damage_from_monster)

            
            # 공격받은 후의 체력 상태 출력
            print(f"\n{monster_to_attack.name}에게 공격받았습니다. 데미지는 {damage_from_monster}입니다.")
            print_health_status(player, monsters)

       elif command == "회복":
           player.heal()
           # 회복 후 체력 상태 출력
           print("\n체력을 회복했습니다.")
           print_health_status(player, monsters)

       
       else:
          print("잘못된 입력입니다. 다시 시도해주세요.")

   # 게임 종료 상태 출력
   if player.health > 0:
      print("\n==== 게임 종료 ====")
      items_string = ', '.join([f'[{item}]' for item in player.inventory])
      items_string += ' 을(를) 얻었습니다.' if len(player.inventory)>1 else ' 을(를) 얻었습니다.'
      
      result_string=f"{player.name}님의 승리!" + items_string
      
      print(result_string)

      
   else:  
      print("\n==== 게임 종료 ====")
      print(f"{player.name}님이 패배하셨습니다.")
      print("아이템을 획득하지 못했습니다.")

if __name__ == "__main__":
   main()
