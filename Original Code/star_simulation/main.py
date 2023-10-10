from star import Star
from constellations import Constellations
import numpy as np
import cv2

def main():
    constellation = Constellations()

    # 별 추가
    sun = Star("태양", 1.989e30, [0, 0, 0], [0, 0, 0])
    earth = Star("지구", 5.972e24, [147e9, 0, 0], [0, 29.29e3, 0])
    constellation.add_star(sun)
    constellation.add_star(earth)

    time_step = 3600  # 1 시간당 시뮬레이션 스텝 (초)

    map = np.full((1000, 1000, 3), 255, np.uint8) # 캔버스 생성

    for _ in range(24 * 365):  # 1년 동안의 시뮬레이션
        constellation.update_positions(time_step)
        print(earth)
        # 지구의 position을 그림에 그리는 코드
        x = int(earth.position[0]/2000000000) # x 좌표 scaling
        y = int(earth.position[1]/2000000000) # y 좌표 scaling
        cv2.line(map, (x, y), (x, y), (0, 0, 255), 1) # 캔버스에 점 찍기
    
    cv2.imshow('map', map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()