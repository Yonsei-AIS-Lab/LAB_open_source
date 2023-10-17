import random

class Player:
    def __init__(self, name, age, position, club, market_value):
        self.name = name
        self.age = age
        self.position = position
        self.club = club
        self.market_value = market_value
        self.stats = {'goals': 0, 'assists': 0}

    def __str__(self):
        return f"{self.name}, {self.age}세, {self.position}, 시장 가치: ${self.market_value}M"

    def transfer(self, new_club, transfer_fee):
        if new_club.budget >= transfer_fee:
            self.club = new_club
            new_club.budget -= transfer_fee
            print(f"{self.name}을(를) {new_club.name}으로 이적했습니다.")
            return True
        else:
            print(f"{new_club.name}의 예산이 부족하여 {self.name}의 이적 거래가 실패했습니다.")
            return False

    def score_goal(self):
        self.stats['goals'] += 1

    def provide_assist(self):
        self.stats['assists'] += 1

class Club:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.squad = []

    def __str__(self):
        return f"{self.name}, 예산: ${self.budget}M"

    def sign_player(self, player, transfer_fee):
        if player.transfer(self, transfer_fee):
            self.squad.append(player)

    def sell_player(self, player):
        if player in self.squad:
            self.squad.remove(player)
            self.budget += player.market_value * 0.8
            print(f"{player.name}을(를) 팔았습니다. {self.name}의 예산: ${self.budget}M")

def main():
    barcelona = Club("FC Barcelona", 200_000_000)
    madrid = Club("Real Madrid", 180_000_000)

    players = [
        Player("Lionel Messi", 34, "Forward", barcelona, 100_000_000),
        Player("Cristiano Ronaldo", 36, "Forward", madrid, 90_000_000),
        Player("Neymar", 29, "Forward", barcelona, 120_000_000),
    ]

    while True:
        print("\n메뉴:")
        print("1. 선수 목록 출력")
        print("2. 선수 이적")
        print("3. 클럽 정보 출력")
        print("4. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            print("\n현재 선수 목록:")
            for player in players:
                print(player)
        elif choice == '2':
            print("\n선수 이적을 위한 클럽 및 이적료를 선택하세요.")
            for i, player in enumerate(players):
                print(f"{i + 1}. {player.name} ({player.club.name}), 시장 가치: ${player.market_value}M")
            
            player_choice = int(input("선수 번호를 입력하세요: ")) - 1
            club_choice = int(input("이적할 클럽 번호를 입력하세요 (1: FC Barcelona, 2: Real Madrid): "))
            transfer_fee = float(input("이적료를 입력하세요 (백만 단위): "))

            if 0 <= player_choice < len(players) and (club_choice == 1 or club_choice == 2):
                if club_choice == 1:
                    barcelona.sign_player(players[player_choice], transfer_fee)
                else:
                    madrid.sign_player(players[player_choice], transfer_fee)
        elif choice == '3':
            print(barcelona)
            print(madrid)
        elif choice == '4':
            break
        else:
            print("올바른 메뉴를 선택하세요.")

if __name__ == "__main__":
    main()