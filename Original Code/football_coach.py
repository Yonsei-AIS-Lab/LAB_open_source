class Player:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level

    def train(self):
        self.skill_level += 1
        print(f"{self.name}의 스킬 레벨이 증가했습니다. 현재 스킬 레벨: {self.skill_level}")

class Coach:
    def __init__(self, name):
        self.name = name

    def assign_player(self, player, team):
        team.add_player(player)
        print(f"{self.name}이 {player.name}을(를) {team.name} 팀에 추가했습니다.")

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def train_players(self):
        for player in self.players:
            player.train()
        print(f"{self.name} 팀의 선수들이 훈련을 받았습니다.")
    
    @classmethod    
    def create_team(cls):
        name = input("팀 이름: ")
        return cls(name)    

# 명령행 인터페이스 (CLI)
def main():
    teams = {}
    coaches = {}
    players = {}

    while True:
        print("\n메뉴:")
        print("1. 선수 추가")
        print("2. 코치 추가")
        print("3. 코치가 선수 팀에 배치")
        print("4. 팀 추가")
        print("5. 팀 훈련")
        print("6. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            name = input("선수 이름: ")
            skill_level = int(input("선수 스킬 레벨: "))
            if skill_level >= 0:
                player = Player(name, skill_level)
                players[name] = player
                print(f"{name} 선수가 추가되었습니다.")
            else:
                raise ValueError("선수 스킬 레벨은 음수가 될 수 없습니다.")

        elif choice == '2':
            name = input("코치 이름: ")
            coach = Coach(name)
            coaches[name] = coach
            print(f"{name} 코치가 추가되었습니다.")

        elif choice == '3':
            coach_name = input("코치 이름: ")
            player_name = input("선수 이름: ")
            team_name = input("팀 이름: ")

            if coach_name in coaches and player_name in players and team_name in teams:
                coach = coaches[coach_name]
                player = players[player_name]
                team = teams[team_name]
                coach.assign_player(player, team)
            else:
                print("코치, 선수 또는 팀을 찾을 수 없습니다.")

        elif choice == '4':
            team = Team.create_team()
            teams[team.name] = team
            print(f"{team.name} 팀이 추가되었습니다.")

        elif choice == '5':
            team_name = input("팀 이름: ")
            if team_name in teams:
                team = teams[team_name]
                team.train_players()
            else:
                print("팀을 찾을 수 없습니다.")

        elif choice == '6':
            break

        else:
            print("잘못된 선택입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()
