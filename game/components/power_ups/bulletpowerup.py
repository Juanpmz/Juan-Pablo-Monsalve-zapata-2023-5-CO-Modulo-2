import random
import pygame.sprite

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SPECIAL_BULLET_BG, BULLET_TYPE
from game.components.bullets.bullet_manager import BulletManager
from game.components.power_ups.power_up import PowerUp

class BulletPowerUp(PowerUp):
    def __init__(self):
        super().__init__(SPECIAL_BULLET_BG, BULLET_TYPE)
       #self.image = image
       #self.bullet_image = bullet_image
       #self.rect = self.image.get_rect()
       #self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
       #self.rect.y = 0
       #self.start_time = 0
       #self.bullet_manager = BulletManager()

    #def update(self, game_speed, power_ups):
    #    self.rect.y += game_speed
    #    if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
    #        power_ups.remove(self)
#
    #def draw(self, screen):
    #    screen.blit(self.image, self.rect)
#
    #def activate_bullets(self):
    #    self.bullet_manager.activate_bullets(self.bullet_image)
    #    self.bullet_manager.add_bullet_from_power_up()
