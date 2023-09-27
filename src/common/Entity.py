from abc import ABC, abstractmethod
import pygame
from pygame.key import ScancodeWrapper
from pygame import Rect
from pygame import Surface
from common.Game import Game
from common.config import Config
from common.sprite import Sprite

class Entity(ABC):
    width: int
    height: int
    color: str | None = None
    rect: Rect
    display: Surface
    current_sprite: Sprite | None

    def __init__(self, x: int, y: int, width: int = None, height: int = None, use_limit: bool = None, gravity_force: float = None) -> None:
        self.current_sprite = None
        self.width = width
        self.height = height
        self._x = x
        self._y = y
        self.gravity_force = gravity_force
        self.use_limit = use_limit
        self.setup()
        self.velocity = pygame.Vector2()
        self.display = pygame.display.get_surface()
        self.init()

    def init(self):
        if self.current_sprite:
            self.rect = self.current_sprite.sprites_rect[0]
            self.height = self.rect.height
            self.width = self.rect.width
            self.rect.move_ip(self._x, self._y)
        else:
            self.rect = pygame.Rect(self._x, self._y, self.width, self.height)


    def gravity(self):
        if not self.gravity_force: return
        gravity = pygame.Vector2(0, self.gravity_force)
        self.velocity += gravity
        self.rect.y += self.velocity.y


    def limit(self):
        if not self.use_limit: return
        WIDTH, HEIGHT = Config.display_size()
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.height))

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def loop(self, keys: ScancodeWrapper, *args):
        pass

    def move(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def render(self, *args):
        keys = pygame.key.get_pressed()
        self.gravity()
        self.loop(keys, *args)
        self.move()
        self.limit()
        if self.current_sprite:
            if len(self.current_sprite.sprites_imgs) > 1:
                sprite = self.current_sprite.animation()
                self.display.blit(sprite, self.rect)
            else:
                sprite_first_img = self.current_sprite.sprites_imgs[0]
                self.display.blit(sprite_first_img, self.rect)
        else:
            pygame.draw.rect(self.display, self.color if self.color else 'white', self.rect)

 