from abc import ABC, abstractmethod
import pygame
import pytmx
from common.Entity import Entity
from common.config import Config
from typing import Mapping, List

class Map(ABC):


    def __init__(self, src: str, collision_tiles: Mapping = None) -> None:
        self.map = pytmx.load_pygame(src)
        self.display = pygame.display.get_surface()
        self.collision_tiles = collision_tiles
        self.collision_gid = []
        self.collision_rect = []
        self.setup_collision_tiles()
    
    def setup_collision_tiles(self):
        if not self.collision_tiles: return
        for tile in self.collision_tiles.values():
            gid = self.get_gid_by_tile(tile)
            self.collision_gid.extend(gid)

    def render(self):
        for layer in self.map.visible_layers:
            for x, y, gid, in layer:
                image = self.map.get_tile_image_by_gid(gid)
                rect = pygame.Rect(x * Config.tile_size(), y * Config.tile_size(), Config.tile_size(), Config.tile_size())
                if image:
                    self.display.blit(image, (x * Config.tile_size(), y * Config.tile_size()))
                if gid in self.collision_gid:
                    self.collision_rect.append(rect)
        

    def get_gid_by_tile(self, tile: int) -> List[int]:
        gids = []
        for key, value in self.map.tiledgidmap.items():
            if value == tile:
                 gids.append(key)
        return gids
                
    @abstractmethod
    def custom_collsion(self):
        pass

    def collision_map_with_entity(self, entity: Entity):
        self.custom_collsion()
        for rect in self.collision_rect:
            if entity.rect.colliderect(rect):
                self.collision_math(entity, rect)
                

    def collision_math(self, entity, rect):
        overlap_x = min(entity.rect.right, rect.right) - max(entity.rect.left, rect.left)
        overlap_y = min(entity.rect.bottom, rect.bottom) - max(entity.rect.top, rect.top)

        if overlap_x < overlap_y:
            if entity.rect.left < rect.left and entity.velocity.x > 0:
                entity.rect.right = rect.left
            elif entity.rect.right > rect.right and entity.velocity.x < 0:
                entity.rect.left = rect.right
            entity.velocity.x = 0
        else:
            if entity.rect.top < rect.top and entity.velocity.y > 0:
                entity.rect.bottom = rect.top
            elif entity.rect.bottom > rect.bottom and entity.velocity.y < 0:
                entity.rect.top = rect.bottom
            entity.velocity.y = 0

    
