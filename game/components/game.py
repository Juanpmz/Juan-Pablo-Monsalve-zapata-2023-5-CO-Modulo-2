import pygame
import time

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, SKIP_BG
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.score_manager import ScoreManager
from game.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu(self.screen)
        self.score = ScoreManager()
        self.death_count = ScoreManager()
        self.highest_score = ScoreManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()

    def draw_background(self):
     image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
     image_height = image.get_height()
     self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
     self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
 
     if self.y_pos_bg >= SCREEN_HEIGHT:
         self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
         self.y_pos_bg = 0

     pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 15, SCREEN_HEIGHT))

     pygame.draw.rect(self.screen, (0, 0, 0), (SCREEN_WIDTH - 15, 0, 15, SCREEN_HEIGHT))

     pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, SCREEN_WIDTH, 10))

     pygame.draw.rect(self.screen, (0, 0, 0), (0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10))

 
     self.y_pos_bg += self.game_speed
 

    def show_menu(self):
     self.menu.reset(self.screen)
     half_screen_width = SCREEN_WIDTH // 2
     half_screen_height = SCREEN_HEIGHT // 2
 
     if self.death_count.count == 0:
         self.menu.draw(self.screen, 'press any key to start')
     else:
         self.update_highest_score()
         self.menu.draw(self.screen, 'Game over. Press any key to restart')
         self.menu.draw(self.screen, f'Your score: {self.score.count}', half_screen_width, 350)
         self.menu.draw(self.screen, f'Highest score: {self.highest_score.count}', half_screen_width, 400)
         self.menu.draw(self.screen, f'Total deaths: {self.death_count.count}', half_screen_width, 450)
 
     pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 15, SCREEN_HEIGHT))
 
     pygame.draw.rect(self.screen, (0, 0, 0), (SCREEN_WIDTH - 15, 0, 15, SCREEN_HEIGHT))

     pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, SCREEN_WIDTH, 10))

     pygame.draw.rect(self.screen, (0, 0, 0), (0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10))
     

 
     icon = pygame.transform.scale(ICON, (80, 120))
     self.screen.blit(icon, (half_screen_width - 50, half_screen_height - 150))
 
     self.menu.update(self)



    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)

    def reset(self):
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.score.reset()
        self.player()
        self.power_up_manager.reset()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                self.menu.draw(self.screen, f'{self.player.power_up_type.capitalize()} is enable for {time_to_show}', 540, 50, (255, 255, 255))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
