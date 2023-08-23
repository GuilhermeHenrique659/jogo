
import pygame
from pygame import Rect
from pygame.key import ScancodeWrapper
from common.Entity import Entity


class Player(Entity):
    def setup(self) -> Rect:
        self.player_vel = 0
        player = pygame.Rect(0, 0, 30, 150)
        return player
    
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