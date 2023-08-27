
import os
import pygame
from pygame import Rect
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.sprite import Sprite


class Player(Entity):
    def setup(self) -> Rect:
        self.player_vel = 0
        self.sprite = Sprite(['assets/player1.png'])
        return self.sprite.get_rect()
    
    def loop(self, keys: ScancodeWrapper):
        if keys[pygame.K_s]:
            self.player_vel = 1
        if keys[pygame.K_w]:
            self.player_vel = -1

        if self.entity.y <= 0:
            self.entity.y = 0
        elif self.entity.y >= self._game.height - 150:
            self.entity.y = self._game.height - 150

        self.entity.y += self.player_vel