# music.py

import pygame

class Music:
    def __init__(self, file):
        self.music = pygame.mixer.Sound(file)

    def play(self):
        self.music.play()

    def stop(self):
        pygame.mixer.stop()