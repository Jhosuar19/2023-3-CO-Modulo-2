import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class Cactus(Obstacle):
    CACTUS = {
        "LARGE": (LARGE_CACTUS),
        "SMALL": (SMALL_CACTUS),
    }

    def __init__(self, image, large = False):
        self.large = large
        self.type = random.randint(0, 2)
        super().__init__(image, self.type) 
        if self.large:
            
            self.rect.y = 305
        else:
            self.rect.y = 325