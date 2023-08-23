import pygame
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.Game import Game
from pong.Ball import Ball
from pong.Player import Player
from pong.Player2 import Player2

class Teste(Entity):
    def setup(self) -> pygame.Rect:
        self.player_vel = 0
        return pygame.Rect(100, 100, 200, 80)
    
    def loop(self, keys: ScancodeWrapper):
        if (keys[pygame.K_w]):
            self.player_vel = 1
        self.entity.x += self.player_vel

class Bar(Game):
    def __init__(self, name: str, width: int, height: int):
        super().__init__(name, width, height)
    
    def setup(self):
        self.fps = 300
        self.player = Player(self)
        self.ball = Ball(self)
        self.player2 = Player2(self)

    def main(self):
        self.display.fill("purple")
        self.player.render()
        self.player2.render(self.ball)
        self.ball.render(self.player, self.player2)

bar = Bar('Bar simulator', 1280, 720)
bar.render()