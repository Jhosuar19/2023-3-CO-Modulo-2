import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.score_manager import ScoreManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.initial_game_speed = 20
        self.game_speed = self.initial_game_speed 
        self.TIME_PER_DAY = 200
        self.time = 0
        self.background_dark_color = False
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu('Press any key to start...', self.screen)
        self.score_manager = ScoreManager(self.screen)
        self.power_up_manager = PowerUpManager(self.screen)
        self.moon_color = (255, 255, 255)
        self.moon_radius = 80
        self.moon_pos = (600, 100)
    
 
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                self.reset()
        pygame.display.quit()
        pygame.quit()


    def run(self):
        pygame.mixer.music.load('dino_runner/assets/Other/Tema_Principal.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.score_manager.reset_score()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.score_manager.draw_score(self.background_dark_color)
        if not self.playing:
            pygame.mixer.music.stop()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input)
            self.score_manager.update_score()
            self.obstacle_manager.update(self)
            self.power_up_manager.update(self)

        if self.score_manager.score % 100 == 0 and self.game_speed < 250:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score_manager.draw_score(self.background_dark_color)
        self.draw_power_up_time(self)
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        self.time +=1
        if self.time >= self.TIME_PER_DAY:
            self.time = 0
            self.background_dark_color = not self.background_dark_color

        if self.background_dark_color:
            self.screen.fill((0,0,0))
        else:
            self.screen.fill((255,255,255))
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        moon_pos_x, moon_pos_y = self.moon_pos
        pygame.draw.circle(self.screen, self.moon_color, (moon_pos_x, moon_pos_y), self.moon_radius)

    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        self.menu.reset_screen_color(self.screen)
        game_over_message = self.score_manager.game_over_message(self.screen)
        if game_over_message:
            self.menu.update_message(game_over_message)


        self.menu.draw(self.screen)

        self.screen.blit(ICON, [half_screen_height + 200 , half_screen_width - 400])

        self.menu.update(self)

    def reset(self):
        self.obstacle_manager.reset()
        self.game_speed = self.initial_game_speed
        self.time = 0
        self.background_dark_color = False
        self.power_up_manager.reset()
    
    def draw_power_up_time(self, screen):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/ 1000, 2)

            if time_to_show >= 0:
                game_font = pygame.font.Font(None, 30)
                game_over_surface = game_font.render(f'{self.player.type.capitalize()} is enable for {time_to_show} seconds', True, (255, 0, 0))
                pos = half_screen_height + 100 , half_screen_width + 200
                self.screen.blit(game_over_surface, pos)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE