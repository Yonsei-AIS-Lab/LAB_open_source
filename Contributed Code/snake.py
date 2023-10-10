import curses
import random

# 게임 화면 설정
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = stdscr.subwin(sh, sw, 0, 0)

w.keypad(1)
w.timeout(100)

# 초기 위치 및 뱀 설정
snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# 먹이 설정
food = [sh // 2, sw // 2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# 방향 설정
key = curses.KEY_RIGHT

# 점수 설정
score = 0

# 게임 루프
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # 게임 종료 조건
    if (
        snake[0][0] in [0, sh] or
        snake[0][1] in [0, sw] or
        snake[0] in snake[1:]
    ):
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    # 방향 설정
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # 먹이 먹기
    if snake[0] == food:
        food = None
        score += 1 # 점수 증가
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    snake.insert(0, new_head)
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

    # 점수 표시
    w.addstr(0, 0, f'Score: {score}')