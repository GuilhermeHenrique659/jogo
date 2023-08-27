from time import sleep
from typing import List

import pygame

from common.Game import Game

class Sprite:
    _game: Game

    def __init__(self, imgs: List[str], **position: any) -> None:
        self.sprites_rect = []
        self.sprites_imgs = []
        self._game = None
        self.init(imgs, **position)

    def get_rect(self):
        return self.sprites_rect[0]

    def init(self, imgs: List[str], **position: any):
        for img in imgs:
            sprite_img = pygame.image.load(img)
            sprite_rect = sprite_img.get_rect(**position)
            self.sprites_rect.append(sprite_rect)
            self.sprites_imgs.append(sprite_img)