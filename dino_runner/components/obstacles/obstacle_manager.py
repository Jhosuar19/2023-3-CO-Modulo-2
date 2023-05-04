import pygame,random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SHIELD_TYPE

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
  def __init__(self):
    self.playing = True
    self.obstacles = []
    self.hit_sound = pygame.mixer.Sound('dino_runner/assets/Other/Está_Muerto.mp3')
    
    
    
  def generate_obstacle(self):
        obstacle = [Cactus(SMALL_CACTUS),Cactus(LARGE_CACTUS), Bird(BIRD)]
        randomObstacle = random.choice(obstacle)
        return randomObstacle
  
  def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
              if game.player.type != SHIELD_TYPE:
                  game.playing = False
                  pygame.time.delay(1000)
                  game.score_manager.death_count += 1
                  self.hit_sound.play()
            elif self.playing:
                  self.hit_sound.stop()
                  break
            else:
                self.obstacles.remove(obstacle)

  def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

  def reset(self):
        self.obstacles = []
