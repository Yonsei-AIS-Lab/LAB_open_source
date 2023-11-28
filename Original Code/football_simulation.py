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
    # 각 팀의 skill의 합의 바탕으로 게임의 승패를 결정하는 코드를 추가함.
    sum_team1_skill = random.randint(0, team1.calculate_team_skill())
    sum_team2_skill = random.randint(0, team2.calculate_team_skill())
    if (sum_team1_skill > sum_team2_skill): # 팀1의 skill 합이 더 높은 경우
        team1_score = random.randint(1, 6)
        team2_score = random.randint(0, 3)
    elif (sum_team1_skill < sum_team2_skill): # 팀2의 skill 합이 더 높은 경우
        team1_score = random.randint(0, 3)
        team2_score = random.randint(1, 6)
    else: # 두 팀의 skill 합이 같은 경우
        team1_score = random.randint(0, 4)
        team2_score = random.randint(0, 4)
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

def create_players(skill):
    players = []
    base_rating = 70
    for idx in range(0, 11):
        rating = base_rating + random.randint(0, skill+1) # random한 능력치 배부
        players.append(Player(f"Player {idx+1}", rating))
    return players

# 선수 생성
team1_skill = int(input("팀 1의 실력을 입력하시오(1~20): "))
players1 = create_players(team1_skill)
team2_skill = int(input("팀 2의 실력을 입력하시오(1~20): "))
players2 = create_players(team2_skill)

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
