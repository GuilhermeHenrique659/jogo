from abc import ABC
from time import sleep
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
                
    def collision_map_with_entity(self, entity: Entity):
        for rect in self.collision_rect:
            if entity.rect.colliderect(rect):
                if entity.rect.left < rect.right and entity.velocity.x > 0:
                    entity.rect.right = rect.left
                elif entity.rect.right > rect.left and entity.velocity.x < 0:
                    entity.rect.left = rect.right

                # Verifica se a colisão ocorre na parte superior ou inferior
                if entity.rect.top < rect.bottom and entity.velocity.y > 0:
                    entity.rect.bottom = rect.top
                elif entity.rect.bottom > rect.top and entity.velocity.y < 0:
                    entity.rect.top = rect.bottom
                entity.velocity.x = 0
                entity.velocity.y = 0

    
