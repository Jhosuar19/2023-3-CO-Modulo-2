import pygame
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER

class Hammer(PowerUp):
    def __init__(self):
        self.type = "hammer"
        self.image = HAMMER
        super().__init__(self.image, self.type)
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 200
