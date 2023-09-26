# music.py

import pygame

class Music:
    def __init__(self, file):
        self.music = pygame.mixer.music.load(file) # pygame.mixer.Sound는 주로 효과음에 사용되므로 배경음악 재생에 사용되는 pygame.mixer.music를 사용

    def play(self):
        self.music.play(-1) # -1은 무한 반복을 의미, 배경음악이 끝나지 않고 계속 재생되도록 함

    def stop(self):
        pygame.mixer.music.stop() #pygame.mixer.stop은 모든 사운드를 정지시키므로 음악만 정지시키는 pygame.mixer.music.stop을 사용