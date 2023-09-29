
from typing import Tuple

from common.config import Config


class Point:
    def __init__(self, point: Tuple[int, int]) -> None:
        self.tile_size = Config.tile_size()
        self.x, self.y = point

    def convert_to_point(self):
        self.x = self.x * self.tile_size
        self.y = self.y * self.tile_size
        return self
    
    def convert_to_tile_address(self):
        self.x = self.x // self.tile_size
        self.y = self.y // self.tile_size
        return self
    
    def compare_tile_y(self, y):
        tile_y = self.y // self.tile_size
        return y == tile_y


    def get_points(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def get_point_tile_address(self) -> Tuple[int, int]:
        tile_x = self.x // self.tile_size
        tile_y = self.y // self.tile_size
        return (tile_x, tile_y)

    def get_point_tile_cordinate(self) -> Tuple[int, int]:
        tile_x = (self.x // self.tile_size) * self.tile_size
        tile_y = (self.y // self.tile_size) * self.tile_size
        return (tile_x, tile_y)
