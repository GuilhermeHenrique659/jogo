
import pygame
from pygame import Rect
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.sprite import Sprite


class Player2(Entity):
    def setup(self) -> Rect:
        self.player_vel = 0
        self.sprite = Sprite(['assets/player2.png'], right=self._game.width)
        return self.sprite.get_rect()
    
    def loop(self, keys: ScancodeWrapper, ball: Entity):
        self.entity.y = ball.entity.y - 75