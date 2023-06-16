import pygame
import time

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.score_manager import ScoreManager

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
        self.menu = Menu('PRESS ANY KEY TO START...', self.screen)
        self.running = False
        self.death_count = 0
        self.score_manager = ScoreManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.score_manager.reset()
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

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
     self.menu.reset(self.screen)
     
     if self.death_count > 0:
         your_score = self.score_manager.get_score()
         highest_score = self.score_manager.get_highest_score()
         total_deaths = self.get_total_deaths()

         message_lines = [
             "Game Over. Press any key to restart",
             f"Your Score: {your_score}",
             f"Highest Score: {highest_score}",
             f"Total Deaths: {total_deaths}"
         ]
         
         y_pos = SCREEN_HEIGHT // 2 - 30  # Posición inicial en el eje Y
         
         for line in message_lines:
             text = self.menu.font.render(line, True, (0, 0, 0))
             text_rect = text.get_rect()
             text_rect.center = (self.menu.HALF_SCREEN_WIDTH, y_pos)
             self.screen.blit(text, text_rect)
             y_pos += 50  # Incremento en la posición Y para la siguiente línea

     half_Screen_width = SCREEN_WIDTH // 2
     half_Screen_height = SCREEN_HEIGHT // 2

     icon = pygame.transform.scale(ICON, (80, 120))
     icon_rect = icon.get_rect()
     icon_rect.center = (half_Screen_width, half_Screen_height - 100)

     self.screen.blit(icon, icon_rect)

     self.menu.draw(self.screen)
     self.screen.blit(icon, icon_rect)
     self.menu.update(self)

     pygame.display.update()

    
        
     
    def update_score(self):
        self.score_manager.increment_score()

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score_manager.get_score()}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_highest_score(self):
       highest_score = self.get_highest_score()
       font = pygame.font.Font(FONT_STYLE, 30)
       text = font.render(f'Highest Score: {highest_score}', True, (255, 255, 255))
       text_rect = text.get_rect()
       text_rect.center = (1000, 100)
       self.screen.blit(text, text_rect )
                           
    def draw_total_deaths(self):
        total_deaths = self.get_total_deaths()
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Total Deaths: {total_deaths}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 150)
        self.screen.blit(text, text_rect)


    def reset(self):
        self.score_manager.reset()
        self.death_count = 0

    def increase_death_count(self):
        self.death_count += 1

    def get_highest_score(self):
        return self.score_manager.get_highest_score()

    def get_total_deaths(self):
        return self.death_count
