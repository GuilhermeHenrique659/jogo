from typing import List
import pygame
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.config import Config
from common.point import Point
from common.sprite import Sprite

class Cursor(Entity):
    def __init__(self, point: Point, positions: List[int]) -> None:
        self.range = range
        self.positions = positions
        self.point = point
        self.index = 0
        x, y = point.get_points()
        super().__init__(x, y)

    def setup(self):
        self.current_sprite = Sprite([
            'assets/bomb/bomb (5).png', 
            'assets/bomb/bomb (4).png', 
            'assets/bomb/bomb (3).png', 
        ])
        self.confirm_sprite = Sprite(['assets/bomb/bomb (2).png'])
        self.confirm_animation_time = 0
        self.confirm_animation_start = False
        self.confirm = False

    def reset(self):
        self.current_sprite = Sprite([
            'assets/bomb/bomb (5).png', 
            'assets/bomb/bomb (4).png', 
            'assets/bomb/bomb (3).png', 
        ])
        self.confirm_animation_time = 0
        self.confirm_animation_start = False
        self.is_alive = True
        self.confirm = False

    def move_cursor(self, pos: int):
        self.index += pos
        if self.index < 0 or self.index >= len(self.positions): return

        y = self.positions[self.index] * Config.tile_size()
        self.point.y = y
        self.rect.y = y
        

    def loop(self, keys: ScancodeWrapper, *args):
        if keys[pygame.K_DOWN]:
            self.move_cursor(+1)
        elif keys[pygame.K_UP]:
            self.move_cursor(-1)
        elif keys[pygame.K_RETURN]:
            self.confirm_animation_start = True
        
        if self.confirm_animation_start:
            self.confirm_animation_time += 1
            self.current_sprite = self.confirm_sprite
            if self.confirm_animation_time >= 40:
                self.kill()
                self.confirm = True
            
