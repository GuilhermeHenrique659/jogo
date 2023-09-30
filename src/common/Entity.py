from abc import ABC, abstractmethod
import pygame
from pygame.key import ScancodeWrapper
from pygame import Rect
from pygame import Surface
from common.config import Config
from common.sprite import Sprite
from typing import Tuple

class Entity(ABC):
    width: int
    height: int
    color: str | None = None
    rect: Rect | None = None
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
        self.init()
        self.velocity = pygame.Vector2()
        self.display = pygame.display.get_surface()
        self.is_alive = True
        self.entities = []

    def init(self):
        if self.current_sprite:
            self.rect = self.current_sprite.sprites_rect[0]
            self.height = self.rect.height
            self.width = self.rect.width
            self.rect.move_ip(self._x, self._y)
        else:
            self.rect = pygame.Rect(self._x, self._y, self.width, self.height)

    def collision_entity(self, orther_entity):
        for entity in orther_entity:
            if not entity or not entity.is_alive: continue
            rect = entity.rect
            if self.rect.colliderect(rect):
                overlap_x = min(self.rect.right, rect.right) - max(self.rect.left, rect.left)
                overlap_y = min(self.rect.bottom, rect.bottom) - max(self.rect.top, rect.top)
                if overlap_x < overlap_y:
                    if self.rect.left < rect.left and self.velocity.x > 0:
                        self.rect.right = rect.left
                    elif self.rect.right > rect.right and self.velocity.x < 0:
                        self.rect.left = rect.right
                    self.velocity.x = 0
                else:
                    if self.rect.top < rect.top and self.velocity.y > 0:
                        self.rect.bottom = rect.top
                    elif self.rect.bottom > rect.bottom and self.velocity.y < 0:
                        self.rect.top = rect.bottom
                    self.velocity.y = 0

    def get_current_tile(self) -> Tuple[int, int]:
        tile_size = Config.tile_size()
        tile_x = (self.rect.x if self.rect else self._x) // tile_size
        tile_y = (self.rect.y if self.rect else self._y) // tile_size
        return (tile_x * tile_size), (tile_y * tile_size)

    def kill(self):
        self.is_alive = False

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
        if not self.is_alive: return

        for entity in self.entities:
            if not entity.is_alive: 
                del entity
                continue
            if entity: entity.render()

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
