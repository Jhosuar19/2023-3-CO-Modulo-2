import random
import pygame
from dino_runner.components.score_manager import ScoreManager
from dino_runner.components.power_ups import shield, hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = random.randint(100,200)
        self.duration = random.randint(3,5)
        self.score_manager = ScoreManager(self)

    def generate_power_up(self):
        power_up_type = random.choice(['shield', 'hammer'])
        if power_up_type == 'shield':
            power_up = shield()
        elif power_up_type == 'hammer':
            power_up = hammer()
        self.when_appers += random.randint(100, 200)
        self.power_ups.append(power_up)

    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appers == self.score_manager.score:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000) 
                self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appers = random.randint(100, 200)
