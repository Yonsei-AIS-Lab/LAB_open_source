import os
import sys
import random

# 미로와 게임 로직
class MazeGame:
    def __init__(self):
        self.maze = [
            "#######",
            "#S    #",
            "#     #",
            "#  ## #",
            "# ### #",
            "#     #",
            "# G### #",
            "#######"
        ]
        self.player_x = 1
        self.player_y = 1
        self.goal_x = 6
        self.goal_y = 2 # 미로 상의 자표와 코드 상의 좌표가 상이하여 수정함
        self.move_count = 0  # 이동 횟수를 기록하는 변수 추가

    def display_maze(self):
        os.system("clear" if sys.platform == "linux" else "cls")  # 화면 지우기

        for i, row in enumerate(self.maze):
            display_row = ""
            for j, col in enumerate(row):
                if i == self.player_x and j == self.player_y:
                    display_row += "P"
                else:
                    display_row += col
            print(display_row)
        print(f"Moves: {self.move_count}")  # 이동 횟수 출력    

    def move(self, direction):
        new_x = self.player_x
        new_y = self.player_y

        if direction == "w":
            new_x -= 1
        elif direction == "s":
            new_x += 1
        elif direction == "a":
            new_y -= 1
        elif direction == "d":
            new_y += 1

        if self.maze[new_x][new_y] != "#":
            self.player_x = new_x
            self.player_y = new_y
            self.move_count += 1  # 이동할 때마다 카운트 증가

    def check_win(self):
        return self.player_x == self.goal_x and self.player_y == self.goal_y

# 게임 실행
def main():
    game = MazeGame()
    game.display_maze()

    while not game.check_win():
        move = input("이동 (w: 위, s: 아래, a: 왼쪽, d: 오른쪽): ")
        game.move(move)
        game.display_maze()

    print("축하합니다! 목표 지점에 도달했습니다.")
    print(f"총 이동 횟수: {game.move_count}")

    # 최단 거리는 시작점(S)에서 도착점(G)까지의 맨해튼 거리로 계산
    shortest_path = abs(game.player_x - 1) + abs(game.player_y - 1)
    print(f"최단 이동 횟수: {shortest_path}")

    if game.move_count == shortest_path:
        print("완벽해요! 최단 거리로 도착했습니다!")
    else:
        print("다음에는 더 짧은 경로로 도전해보세요!")

if __name__ == "__main__":
    main()
