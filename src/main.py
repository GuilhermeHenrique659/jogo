import pygame
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.Game import Game

class Teste(Entity):
    def setup(self) -> pygame.Rect:
        return pygame.Rect(100, 100, 200, 80)
    
    def loop(self, keys: ScancodeWrapper):
        if (keys[pygame.K_w]):
            self.entity.x += 10

class Bar(Game):
    def __init__(self, name: str, width: int, height: int):
        super().__init__(name, width, height)
    
    def setup(self):
        self.teste = Teste(self)

    def main(self):
        self.display.fill("purple")
        self.teste.render()

bar = Bar('Bar simulator', 1280, 720)
bar.render()