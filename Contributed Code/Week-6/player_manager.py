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
    
    def get_formations(self):
        print("4-4-2\n")

    def get_Forward(self):
        return [player for player in self.players if player.position == "공격수"]
    
    def get_Midfielder(self):
        return [player for player in self.players if player.position == "미드필더"]
    
    def get_Defender(self):
        return [player for player in self.players if player.position == "수비수"]
    
    def get_Goalkeeper(self):
        return [player for player in self.players if player.position == "골키퍼"]

# 선수 생성
player1 = Player("선수1", 25, "공격수")
player2 = Player("선수2", 28, "수비수")
player3 = Player("선수3", 22, "미드필더")
player4 = Player("선수4", 21, "미드필더")
player5 = Player("선수5", 27, "미드필더")
player6 = Player("선수6", 23, "미드필더")
player7 = Player("선수7", 24, "공격수")
player8 = Player("선수8", 26, "수비수")
player9 = Player("선수9", 29, "수비수")
player10 = Player("선수10", 30, "수비수")
player11 = Player("선수11", 31, "골키퍼")


# 팀 생성
team = Team("팀 A")

# 포메이션
print("포메이션:")
team.get_formations()

# 선수 팀에 추가
team.add_player(player1)
team.add_player(player2)
team.add_player(player3)
team.add_player(player4)
team.add_player(player5)
team.add_player(player6)
team.add_player(player7)
team.add_player(player8)
team.add_player(player9)
team.add_player(player10)
team.add_player(player11)

# 선수 부상 처리
player1.is_injured = True
player2.is_injured = True
player6.is_injured = True
player8.is_injured = True
player9.is_injured = True

# 선수 목록 출력
print("팀 A 선수 목록:")
team.list_players()

print("\n공격수 목록:")
forward = team.get_Forward()
for player in forward:
    print(player.introduce())

print("\n미드필더 목록:")
midfielder = team.get_Midfielder()
for player in midfielder:
    print(player.introduce())

print("\n수비수 목록:")
defender = team.get_Defender()
for player in defender:
    print(player.introduce())

print("\n골키퍼 목록:")
goalkeeper = team.get_Goalkeeper()
for player in goalkeeper:
    print(player.introduce())

# 부상자 목록 출력
print("\n부상자 목록:")
injured_players = team.get_injured_players()
for player in injured_players:
    print(player.introduce())
