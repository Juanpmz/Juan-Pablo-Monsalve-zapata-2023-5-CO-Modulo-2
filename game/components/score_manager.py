import pygame
import time

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE


class ScoreManager:
    def __init__(self):
        self.score = 0
        self.highest_score = 0
        self.start_time = 0

    def start_timer(self):
        self.start_time = time.time()

    def reset(self):
        self.score = 0
        self.start_time = 0

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def get_highest_score(self):
        return self.highest_score

    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score

        return self.highest_score
