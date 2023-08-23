from time import sleep
from typing import List

import pygame

from common.Game import Game

class Sprite:
    _game: Game

    def __init__(self, imgs: List[str], game: Game) -> None:
        self.sprites_rect = []
        self.sprites_imgs = []
        self._game = game
        self.init(imgs)

    def init(self, imgs: List[str]):
        for img in imgs:
            sprite_img = pygame.image.load(img)
            sprite_rect = sprite_img.get_rect()
            self.sprites_rect.append(sprite_rect)
            self.sprites_imgs.append(sprite_img)

    def get_firts(self):
        return self.sprites_rect[0]
    
    def get_sprits(self):
        return self.sprites_rect
    
    def animation(self):
        delay = 16
        for i in range(self.sprites_rect):
            sleep(self._game.fps / delay)
            self._game.display.blit(self.sprites_imgs[i],  self.sprites_rect[i])