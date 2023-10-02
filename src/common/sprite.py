import time
from typing import Tuple, List

import pygame

from common.Game import Game
from common.config import Config

class Sprite:
    def __init__(self, imgs: List[str], position: Tuple[int, int] = None, tick = 200) -> None:
        self.sprites_rect: List[pygame.Rect] = []
        self.sprites_imgs: List[pygame.Surface] = []
        self.init(imgs)
        self.tick = tick
        self.current_index = 0
        self.last_update_time = 0
        self.is_fliped = False

    def scale_tile(self):
        new_sprites_imgs = []
        new_rects = []
        for img in self.sprites_imgs:
            new_img = pygame.transform.scale(img, (Config.tile_size(), Config.tile_size()))
            new_rects.append(new_img.get_rect())
            new_sprites_imgs.append(new_img)
        self.sprites_rect = new_rects
        self.sprites_imgs = new_sprites_imgs

    def init(self, imgs: List[str]):
        for img in imgs:
            sprite_img = pygame.image.load(img).convert_alpha()
            sprite_rect = sprite_img.get_rect()
            self.sprites_rect.append(sprite_rect)
            self.sprites_imgs.append(sprite_img)
    
    def flip(self, flip_x = False, flip_y = False):
        images_fliped = []
        for image in self.sprites_imgs:
            image = pygame.transform.flip(image, flip_x, flip_y)
            images_fliped.append(image)
        self.sprites_imgs = images_fliped
        self.is_fliped = not self.is_fliped

    def animation(self) -> pygame.Surface:
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time >= self.tick:
            self.last_update_time = current_time
            self.current_index = (self.current_index + 1) % len(self.sprites_imgs)

        return pygame.transform.scale(self.sprites_imgs[self.current_index], (self.sprites_rect[self.current_index].size))
        