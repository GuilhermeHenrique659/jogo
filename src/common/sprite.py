import time
from typing import Tuple, List

import pygame

from common.Game import Game

class Sprite:
    def __init__(self, imgs: List[str], position: Tuple[int, int] = None, tick = 200) -> None:
        self.sprites_rect: List[pygame.Rect] = []
        self.sprites_imgs: List[pygame.Surface] = []
        self.init(imgs)
        self.tick = tick
        self.current_index = 0
        self.last_update_time = 0

    def init(self, imgs: List[str]):
        for img in imgs:
            sprite_img = pygame.image.load(img)
            sprite_rect = sprite_img.get_rect()
            self.sprites_rect.append(sprite_rect)
            self.sprites_imgs.append(sprite_img)
    
    def animation(self) -> pygame.Surface:
        current_time = pygame.time.get_ticks()

        if current_time - self.last_update_time >= self.tick:
            self.last_update_time = current_time
            self.current_index = (self.current_index + 1) % len(self.sprites_imgs)

        return pygame.transform.scale(self.sprites_imgs[self.current_index], (self.sprites_rect[self.current_index].size))
        