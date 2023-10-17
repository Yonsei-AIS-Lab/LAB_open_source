import random

class Player:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0

    def calculate_team_skill(self):
        return sum(player.skill for player in self.players)

def simulate_game(team1, team2):
    team1_score = random.randint(0, 5)
    team2_score = random.randint(0, 5)
    team1.score += team1_score
    team2.score += team2_score
    return f"{team1.name} {team1_score} - {team2.name} {team2_score}"

def print_scoreboard(team1, team2):
    print(f"{team1.name}: {team1.score} - {team2.name}: {team2.score}")

def determine_winner(team1, team2):
    if team1.score > team2.score:
        return f"{team1.name}이(가) 이겼습니다!"
    elif team2.score > team1.score:
        return f"{team2.name}이(가) 이겼습니다!"
    else:
        return "무승부입니다!"

def print_team_skills(team1, team2):
    print("\n팀 스킬 레벨:")
    print(f"{team1.name}: {team1.calculate_team_skill()}")
    print(f"{team2.name}: {team2.calculate_team_skill()}")

def play_game(num_games):
    # 여러 번의 경기 시뮬레이션 실행
    for game in range(num_games):
        print(f"\nGame {game + 1}: {simulate_game(team1, team2)}")

    # 경기 결과 및 통계 출력
    print("\nFinal Score:")
    print_scoreboard(team1, team2)
    print(determine_winner(team1, team2))

# 선수 생성
players1 = [Player("Player 1", 80), Player("Player 2", 85), Player("Player 3", 75)]
players2 = [Player("Player 4", 78), Player("Player 5", 82), Player("Player 6", 79)]

# 팀 생성
team1 = Team("Team A", players1)
team2 = Team("Team B", players2)



# 추가 기능: 팀 스킬 레벨 출력
while True:
    user_choice = input("\n추가 기능 선택 (0: 게임 실행, 1: 팀 스킬 레벨, 2: 종료): ")
    if user_choice == '1':
        print_team_skills(team1, team2)
    elif user_choice == '2':
        break
    elif user_choice == '0':
        num_game = int(input("실행하고 싶은 경기 수를 입력하시오: "))
        play_game(num_game)
    else:
        print("잘못된 선택입니다. 다시 선택하세요.")