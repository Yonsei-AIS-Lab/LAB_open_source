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
        self.is_home = 0

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

    team1_is_home = random.randint(0, 1)
    if team1_is_home == 1:
        team1_score += 1
        team1.is_home = 1
        team2.is_home = 0
    else:
        team2_score += 1
        team2.is_home = 1
        team1.is_home = 0
    team1.score += team1_score
    team2.score += team2_score
    return f"{team1.name} {team1_score} - {team2.name} {team2_score} : {get_home_stadium(team1, team2)}"

def get_home_stadium(team1, team2):
    if team1.is_home == 1:
        return f"{team1.name}의 홈 경기"
    else:
        return f"{team2.name}의 홈 경기"

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
def play_game(num_games):
    # 여러 번의 경기 시뮬레이션 실행
    for game in range(num_games):
        print(f"\nGame {game + 1}: {simulate_game(team1, team2)}")

    # 경기 결과 및 통계 출력
    print("\nFinal Score:")
    print_scoreboard(team1, team2)
    print(determine_winner(team1, team2))

# 선수 생성
team1_skill = int(input("팀 1의 실력을 입력하시오(1~20): "))
players1 = create_players(team1_skill)
team2_skill = int(input("팀 2의 실력을 입력하시오(1~20): "))
players2 = create_players(team2_skill)

# 팀 생성
team1 = Team("Team A", players1)
team2 = Team("Team B", players2)



def transfer(team):
    print('컴퓨터와 가위, 바위, 보를 해서 이기면 선수를 영입할 수 있습니다.')
    your_choice = int(input("가위=0, 바위=1, 보=2: "))
    pc_choice = random.randint(0, 3)
    if your_choice == 0 and pc_choice == 2 or your_choice == 1 and pc_choice == 0 or your_choice == 2 and pc_choice == 1:
        print("축하드립니다. 이겼습니다!")
        len_team = len(team.players)
        # 팀의 마지막 선수를 호날두로 교채
        team.players[len_team-1] = Player("호X두", 100)
        print("현재 팀의 모습입니다!")
        for idx in range(0, len_team):
            print(f"선수이름: {team.players[idx].name}, 선수 능력치: {team.players[idx].skill}")
    else:
        print("못 이겼습니다 ㅋㅋ")

# 추가 기능: 팀 스킬 레벨 출력
while True:
    user_choice = input("\n추가 기능 선택 (1: 팀 스킬 레벨, 2: 종료, 3: 선수 영입): ")
    if user_choice == '1':
        print_team_skills(team1, team2)
    elif user_choice == '2':
        break
    elif user_choice == '0':
        num_game = int(input("실행하고 싶은 경기 수를 입력하시오: "))
        play_game(num_game)
    elif user_choice == '3':
        select_team = int(input("선수를 영입할 팀을 선택하시오 (1, 2):"))
        if select_team ==  1:
            transfer(team1)
        else:
            transfer(team2)
    else:
        print("잘못된 선택입니다. 다시 선택하세요.")