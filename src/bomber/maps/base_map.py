

from typing import Mapping
from common.map import Map


class BaseMap(Map):
    def __init__(self, src: str, collision_tiles: Mapping = None) -> None:
        super().__init__(src, collision_tiles)