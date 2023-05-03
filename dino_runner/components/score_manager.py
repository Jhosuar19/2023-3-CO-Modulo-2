import pygame
import os
from dino_runner.utils.constants import FONT_STYLE

class ScoreManager:

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.highest_score = 0
        self.game_speed = 30
        self.death_count = 0

    def update_score(self):
        self.score += 1
        if self.score > self.highest_score:
            self.highest_score = self.score

        if self.score % 100 == 0 and self.game_speed < 250:
            self.game_speed += 5

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True,(0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        self.screen.blit(text, text_rect)

    def reset_score(self):
        self.score = 0

    def game_over_message(self):
        return f'Game over press any key to restart.{os.linesep}' \
               f'Highest score: {self.highest_score}{os.linesep}' \
               f'Your score: {self.score}{os.linesep}' \
               f'Total deaths: {self.death_count}.'


