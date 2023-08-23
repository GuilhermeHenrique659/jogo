from abc import ABC, abstractmethod
import pygame
from pygame.key import ScancodeWrapper
from pygame import Rect
from pygame import Surface

from common.Game import Game

class Entity(ABC):
    weight: int
    height: int
    entity: Rect
    display: Surface
    _game: Game

    def __init__(self, game: Game) -> None:
        self._game = game
        self.entity = self.setup()

    @abstractmethod
    def setup(self) -> Rect:
        pass

    @abstractmethod
    def loop(self, keys: ScancodeWrapper, *args):
        pass

    def render(self, *args):
        keys = pygame.key.get_pressed()
        self.loop(keys, *args)
        pygame.draw.rect(self._game.display, 'white', self.entity)
 