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
    # 일정한 확률에 따라 주심이 오심을 해서 골이 취소되는 코드를 추가했습니다.
    prob_mis = random.randint(0, 10)
    if prob_mis > 8: # 10%의 확률에 해당하면
        team_fail = random.randint(0, 2)
        if team_fail == 0: # 팀1이 억울하게 취소당한 경우
            if team1_score > 0:
                team1_score -= 1
                print("주심에 오심으로 팀1의 골이 인정되지 않았습니다!")
        else:
            if team2_score > 0:
                team2_score -= 1
                print("주심에 오심으로 팀2의 골이 인정되지 않았습니다!")
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

# 선수 생성
players1 = [Player("Player 1", 80), Player("Player 2", 85), Player("Player 3", 75)]
players2 = [Player("Player 4", 78), Player("Player 5", 82), Player("Player 6", 79)]

# 팀 생성
team1 = Team("Team A", players1)
team2 = Team("Team B", players2)

# 여러 번의 경기 시뮬레이션 실행
num_games = 10
for game in range(num_games):
    print(f"\nGame {game + 1}: {simulate_game(team1, team2)}")

# 경기 결과 및 통계 출력
print("\nFinal Score:")
print_scoreboard(team1, team2)
print(determine_winner(team1, team2))

# 추가 기능: 팀 스킬 레벨 출력
while True:
    user_choice = input("\n추가 기능 선택 (1: 팀 스킬 레벨, 2: 종료): ")
    if user_choice == '1':
        print_team_skills(team1, team2)
    elif user_choice == '2':
        break
    else:
        print("잘못된 선택입니다. 다시 선택하세요.")
