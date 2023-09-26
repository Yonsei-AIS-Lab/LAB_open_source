# main.py

import pygame
from game import Game

if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    game = Game()
    game.run()
