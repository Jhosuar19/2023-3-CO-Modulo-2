import pygame

from dino_runner.utils.constants import FONT_STYLE,SCREEN_HEIGHT,SCREEN_WIDTH

class ScoreManager:

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.highest_score = 0
        self.death_count = 0
        self.is_daytime = True

    def update_score(self):
        self.score += 1
        if self.score > self.highest_score:
            self.highest_score = self.score


    def draw_score(self, is_daytime):
        font = pygame.font.Font(FONT_STYLE, 30)
        if is_daytime:
            text_color = (255, 255, 255)
        else:
            text_color = (0, 0, 0)
        text = font.render(f'Score: {self.score}', True, text_color)
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        self.screen.blit(text, text_rect)

    def reset_score(self):
        self.score = 0

    def game_over_message(self,screen):
        if self.death_count >= 1:
            half_screen_height = SCREEN_HEIGHT // 2
            half_screen_width = SCREEN_WIDTH // 2
            game_font = pygame.font.Font(None, 30)
            game_over_surface = game_font.render(f'GAME OVER', True, (255, 0, 0))
            pos = half_screen_height + 185 , half_screen_width - 450 
            screen.blit(game_over_surface, (pos))
            game_over_surface = game_font.render(f'Highest score: {self.highest_score}', True, (0, 0, 0))
            pos = half_screen_height + 170 , half_screen_width - 200
            screen.blit(game_over_surface, (pos))
            game_over_surface = game_font.render(f'Your score: {self.score}', True, (0, 0, 0))
            pos = half_screen_height + 175 , half_screen_width - 170
            screen.blit(game_over_surface, (pos))
            game_over_surface = game_font.render(f'Total deaths: {self.death_count}', True, (0, 0, 0))
            pos = half_screen_height + 175 , half_screen_width - 140
            screen.blit(game_over_surface, (pos))