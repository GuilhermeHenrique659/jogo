import pygame
from pygame import Rect
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.sprite import Sprite


class Ball(Entity):
    def setup(self) -> Rect:
        self.sprite = Sprite(['assets/ball.png'], right=self._game.height/2, top=self._game.width/2)
        self.ball_dir_x = 1
        self.ball_dir_y = 1
        return self.sprite.get_rect()
    
    def ball_behavior(self):
        if self.entity.x <= 0:
            self.entity.x = 600
            self.ball_dir_x *= -1
        elif self.entity.x >= self._game.width:
            self.entity.x = 600
            self.ball_dir_x *= -1
        if self.entity.y <= 0:
            self.ball_dir_y *= -1
        elif self.entity.y >= self._game.height:
            self.ball_dir_y *= -1
    
    def loop(self, keys: ScancodeWrapper, player1: Entity, player2: Entity):
        if self.entity.colliderect(player1.entity) or self.entity.colliderect(player2.entity):
            self.ball_dir_x *= -1
        self.ball_behavior()

        self.entity.x += self.ball_dir_x
        self.entity.y += self.ball_dir_y