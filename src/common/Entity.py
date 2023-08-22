from abc import ABC, abstractmethod
import pygame
from pygame.key import ScancodeWrapper
from pygame import Rect
from pygame import Surface

from common.Game import Game

class Entity(ABC):
    x: int
    y: int
    weight: int
    height: int
    entity: Rect
    display: Surface
    __game: Game

    def __init__(self, game: Game) -> None:
        self.__game = game
        self.entity = self.setup()

    @abstractmethod
    def setup(self) -> Rect:
        pass

    @abstractmethod
    def loop(self, keys: ScancodeWrapper):
        pass

    def render(self):
        keys = pygame.key.get_pressed()
        self.loop(keys)
        pygame.draw.rect(self.__game.display, 'red', self.entity)

 