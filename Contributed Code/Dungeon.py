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
    def __init__(self, name):
        self.name = name
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

def main():
    
   player_name = input("플레이어 이름을 입력하세요: ")
   player = Player(player_name)
   
   monsters = [Monster("고블린"), Monster("드래곤"), Monster("스켈레톤")]
   
   print("\n==== 게임 시작 ====")
   print(f"{player.name}님의 초기 체력: {player.health}") 
   
   for monster in monsters:
       print(f"몬스터 {monster.name}의 초기 체력: {monster.health}")
       
   print("=================\n")
   
   
   while player.health > 0:
       command = input("\n[명령 선택]\n1) 공격\n2) 회복\n3) 나가기\n명령어를 입력하세요: ")
       print("-----------------\n")
       

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
                print(f"{monster_to_attack.name}을(를) 처치하였습니다!")
                player.inventory.append(f"{monster_to_attack.name}의 아이템")
                
                alive_monsters_after_attack = [monster for monster in monsters if monster.health > 0]
                
                if not alive_monsters_after_attack: 
                    print("모든 몬스터를 처치하셨습니다! 게임에서 승리하셨습니다.")
                    return
            
            else: 
                for monster in monsters:
                     print(f"몬스터 {monster.name}의 남은 체력: {monster.health}")
   
            
            damage_from_monster = monster_to_attack.attack()
            player.take_damage(damage_from_monster)
            
            print("-----------------\n")
            print(f"{monster_to_attack.name}이(가) {player.name}님을 공격하여 {damage_from_monster}의 데미지를 주었습니다!")
        
            # 플레이어 체력 상태 출력
            print(f"플레이어 {player.name}의 남은 체력: {player.health}")

       elif command == "회복":
           player.heal()
           print(f"{player.name}님이 회복하였습니다. 현재 체력: {player.health}")
       
       else:
          print("잘못된 입력입니다. 다시 시도해주세요.")
        
       print("=================\n")
        

   # 게임 종료 상태 출력
   if player.health > 0:
      print("\n==== 게임 종료 ====")
      print(f"{player.name}님의 승리! 획득한 아이템: {', '.join(player.inventory)}")
   else:
      print("\n==== 게임 종료 ====")
      print(f"{player.name}님이 패배하셨습니다.")
      print("아이템을 획득하지 못했습니다.")

if __name__ == "__main__":
   main()
