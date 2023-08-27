from abc import ABC, abstractmethod
import pygame
from pygame.key import ScancodeWrapper
from pygame import Rect
from pygame import Surface
from common.Game import Game
from common.sprite import Sprite

class Entity(ABC):
    weight: int
    height: int
    entity: Rect
    display: Surface
    sprite: Sprite | None
    _game: Game

    def __init__(self, game: Game) -> None:
        self._game = game
        self.sprite = None
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
        if self.sprite:
            if len(self.sprite.sprites_imgs) > 1:
                self.sprite._game = self._game
                self.sprite.animation()
            else:
                sprite_first_img = self.sprite.sprites_imgs[0]
                self._game.display.blit(sprite_first_img, self.entity)
        else:
            pygame.draw.rect(self._game.display, 'white', self.entity)

 