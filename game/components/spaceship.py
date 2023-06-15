import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT
class Spaceship(Sprite):
  SPACESHIP_WIDTH = 40
  SPACESHIP_HEIGHT = 60
  HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
  X_POS = (SCREEN_HEIGHT // 2) - SPACESHIP_WIDTH
  Y_POS = 500
  SHOOT_DELAY = 200

  def __init__(self):
    self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
    self.rect = self.image.get_rect()
    self.rect.x = self.X_POS
    self.rect.y = self.Y_POS
    self.bullet_rect = pygame.Rect(0, 0, 10, 10)
    self.bullet_color = (255, 255, 0)
    self.bullet_speed = 45
    self.bullet = None
    self.type = 'player'

  def update(self, user_input):
    if user_input[pygame.K_LEFT]:
      self.move_left()
    elif user_input[pygame.K_RIGHT]:
      self.move_right()
    elif user_input[pygame.K_UP]:
      self.move_up()
    elif user_input[pygame.K_DOWN]:
      self.move_down()
    elif user_input[pygame.K_SPACE]:
      self.shoot_bullet()

    self.update_bullet()

  def move_left(self):
    self.rect.x = (self.rect.x - 10) % (SCREEN_WIDTH - self.SPACESHIP_WIDTH)

  def move_right(self):
      self.rect.x = (self.rect.x + 10) % (SCREEN_WIDTH - self.SPACESHIP_WIDTH)

  def move_up(self):
    if self.rect.y > self.HALF_SCREEN_HEIGHT:
     self.rect.y -=10

  def move_down(self):
    if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEIGHT:
     self.rect.y +=10

  def shoot_bullet(self):
        bullet_x = self.rect.centerx - self.bullet_rect.width // 2
        bullet_y = self.rect.y
        self.bullet = (bullet_x, bullet_y)

  def update_bullet(self):
      if self.bullet is not None:
          self.bullet = (self.bullet[0], self.bullet[1] - self.bullet_speed)
          if self.bullet[1] + self.bullet_rect.height < 0:
              self.bullet = None
  def remove_enemy(self, enemy, enemies):
     if enemy in enemies:
       enemies.remove(enemy)

  def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.bullet is not None:
            pygame.draw.rect(screen, self.bullet_color, pygame.Rect(*self.bullet, *self.bullet_rect.size))