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

    # Monster takes damage by reducing health.
    def take_damage(self, damage):   
         self.health -= damage
         if self.health < 0: # If health falls below zero,
             self.health = 0 # set it to zero.

def main():
    
   player_name = input("플레이어 이름을 입력하세요: ")
   player = Player(player_name)
   
   monsters = [Monster("고블린"), Monster("드래곤"), Monster("스켈레톤")]
   
   print(f"{player.name}님의 초기 체력: {player.health}") # Print the initial health of the player
   
   for monster in monsters:
       print(f"몬스터 {monster.name}의 초기 체력: {monster.health}") # Print the initial health of each monster
   
   
   while player.health > 0:
       command = input("어떤 행동을 하시겠습니까? (공격/회복/나가기): ").lower()

       if command == "나가기":
            print("게임에서 나갑니다.")
            
            if len(player.inventory) == 0:
                print(f"{player.name}님이 획득한 아이템이 없습니다.") #"나가기" to print the acquired item
            else:
                print(f"{player.name}님의 승리! 획득한 아이템: {', '.join(player.inventory)}") #"나가기" to print the acquired item
            
            return 
       
       elif command == "공격":
            alive_monsters = [monster for monster in monsters if monster.health > 0] # Select only alive monsters
            
            if not alive_monsters: # If there are no alive monsters,
                print("모든 몬스터를 처치하셨습니다!")
                break
            
            monster_to_attack= random.choice(alive_monsters)
            
            damage_to_monster= player.attack()
            
            monster_to_attack.take_damage(damage_to_monster)
           
            if monster_to_attack.health <= 0:
                print(f"{monster_to_attack.name}을(를) 처치하였습니다!")
                player.inventory.append(f"{monster_to_attack.name}의 아이템")
                
                # Check again after attacking if all monsters are defeated.
                alive_monsters_after_attack = [monster for monster in monsters if monster.health > 0]
                
                if not alive_monsters_after_attack: 
                    print("모든 몬스터를 처치하셨습니다! 게임에서 승리하셨습니다.")
                    return
            
            else: 
                for monster in monsters:
                     print(f"몬스터 {monster.name}의 남은 체력: {monster.health}") # Print the remaining health of each monster
   
            
            damage_from_monster = monster_to_attack.attack()
            player.take_damage(damage_from_monster)
            
            print(f"{monster_to_attack.name}이(가) {player.name}님을 공격하여 {damage_from_monster}의 데미지를 주었습니다!")
            print(f"플레이어 {player.name}의 남은 체력: {player.health}")

       elif command == "회복":
           player.heal()
           print(f"{player.name}님이 회복하였습니다. 현재 체력: {player.health}")
       
       else:
          print("잘못된 입력입니다. 다시 시도해주세요.")

   if player.health > 0:
      print("게임이 종료되었습니다.")
      print(f"{player.name}님의 승리! 획득한 아이템: {', '.join(player.inventory)}")
   else: #player's health is 0
      print("게임이 종료되었습니다.")
      print(f"{player.name}님이 패배하셨습니다.")
      print("아이템을 획득하지 못했습니다.")

if __name__ == "__main__":
   main()
