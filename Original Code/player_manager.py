class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.is_injured = False

    def introduce(self):
        return f"이름: {self.name}, 나이: {self.age}, 포지션: {self.position}, 부상 여부: {'부상 중' if self.is_injured else '미부상'}"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def list_players(self):
        for player in self.players:
            print(player.introduce())

    def get_injured_players(self):
        return [player for player in self.players if player.is_injured]

# 선수 생성
player1 = Player("선수1", 25, "공격수")
player2 = Player("선수2", 28, "수비수")
player3 = Player("선수3", 22, "미드필더")

# 팀 생성
team = Team("팀 A")

# 선수 팀에 추가
team.add_player(player1)
team.add_player(player2)
team.add_player(player3)

# 선수 목록 출력
print("팀 A 선수 목록:")
team.list_players()

# 선수 부상 처리
player1.is_injured = True
player2.is_injured = True

# 부상자 목록 출력
print("\n부상자 목록:")
injured_players = team.get_injured_players()
for player in injured_players:
    print(player.introduce())
