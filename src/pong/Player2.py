
import pygame
from pygame import Rect
from pygame.key import ScancodeWrapper
from common.Entity import Entity


class Player2(Entity):
    def setup(self) -> Rect:
        self.player_vel = 0
        player = pygame.Rect(1250, 0, 30, 150)
        return player
    
    def loop(self, keys: ScancodeWrapper, ball: Entity):
        self.entity.y = ball.entity.y - 75