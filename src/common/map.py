from abc import ABC
import pygame
import pytmx
from common.Entity import Entity
from common.config import Config
from typing import Mapping

class Map(ABC):


    def __init__(self, src: str, collision_tiles: Mapping) -> None:
        self.map = pytmx.load_pygame(src)
        self.display = pygame.display.get_surface()
        self.collision_tiles = collision_tiles
        self.collision_gid = []
        self.collision_rect = []
        self.setup()
    
    def setup(self):
        for tile in self.collision_tiles.values():
            gid = self.get_gid_by_tile(tile)
            self.collision_gid.append(gid)
        print(self.collision_gid)

    def render(self):
        for layer in self.map.visible_layers:
            for x, y, gid, in layer:
                image = self.map.get_tile_image_by_gid(gid)
                rect = pygame.Rect(x * Config.tile_size(), y * Config.tile_size(), Config.tile_size(), Config.tile_size())
                if image:
                    self.display.blit(image, (x * Config.tile_size(), y * Config.tile_size()))
                if gid in self.collision_gid:
                    self.collision_rect.append(rect)
        

    def get_gid_by_tile(self, tile: int) -> int:
        for key, value in self.map.tiledgidmap.items():
            if value == tile:
                return key
        
