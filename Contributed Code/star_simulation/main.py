from star import Star
from constellations import Constellations

def main():
    constellation = Constellations()

    # 별 추가
    sun = Star("태양", 1.989e30, [0, 0, 0], [0, 0, 0])
    earth = Star("지구", 5.972e24, [147e9, 0, 0], [0, 29.29e3, 0])
    constellation.add_star(sun)
    constellation.add_star(earth)

    time_step = 3600  # 1 시간당 시뮬레이션 스텝 (초)

    for _ in range(24 * 365):  # 1년 동안의 시뮬레이션
        constellation.update_positions(time_step)
        print(earth)

if __name__ == "__main__":
    main()