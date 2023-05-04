import pygame
from dino_runner.components.power_ups.power_up import PowerUp

class Hammer(PowerUp):
    def __init__(self):
        super().__init__()
        self.type = "hammer"
        self.image = pygame.image.load("assets/images/power_ups/hammer.png")
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 200
