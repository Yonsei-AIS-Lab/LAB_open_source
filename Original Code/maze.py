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
        self.goal_y = 2 # 화면에 표시된 미로의 좌표와 실제 미로의 좌표가 달라서 화면에 표시된 좌표를 기준으로 수정함

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

if __name__ == "__main__":
    main()
