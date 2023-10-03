# game.py

import pygame
import os
from player import Player
from obstacle import Obstacle
from music import Music
import random
import librosa

class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Rhythm Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player()
        self.obstacles = []
        self.music = Music("./Contributed Code/Week-3/Music Tab Bilgee/background_music.wav")
        self.beat_times = self.detect_beats()
    
    def detect_beats(self):
        y, sr = librosa.load("./Contributed Code/Week-3/Music Tab Bilgee/background_music.wav")
        onset_env = librosa.onset.onset_strength(y=y, sr= sr)
        tempo, beat_frames = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        return beat_times

    def run(self):
        self.music.play()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.tap()

    def spawn_obstacles(self):
        current_time = pygame.time.get_ticks() / 1000 
        if self.beat_times.any() and abs(current_time - self.beat_times[10]) < 0.05:
            x = random.randint(0, self.screen_width - 30)
            speed = 15
            self.obstacles.append(Obstacle(x, speed))
            self.beat_times = self.beat_times[1:]

    def update(self):
        self.obstacles = [obstacle for obstacle in self.obstacles if not obstacle.collide(self.player)]
        self.player.update()
        self.spawn_obstacles()
        for obstacle in self.obstacles:
            obstacle.move()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
