

import random
from typing import Mapping
from bomber.maps.destructionBlock import DestructionBlock
from common.Entity import Entity
from common.concurrancyForEach import concurrancy_for_each
from common.config import Config
from common.map import Map
from typing import List


class BaseMap(Map):
    def __init__(self, src: str, collision_tiles: Mapping = None, n_destruction_blocks = 120) -> None:
        self.n_destruction_blocks = n_destruction_blocks
        self.destruction_blocks: List[Entity] = []
        super().__init__(src, collision_tiles)

    def render_destruction_blocks(self):
        for entity in self.destruction_blocks:
            entity.render()

    def __generate_cordinate(self):
        tile_size = Config.tile_size()
        width, height = Config.display_size()
        block_x = random.randrange(tile_size, width - tile_size, tile_size)
        block_y = random.randrange(tile_size, height - tile_size, tile_size)
        return (block_x, block_y)

    def generate_destruction_blocks(self, player1: Entity, player2: Entity):
        tile_size = Config.tile_size()
        width, height = Config.display_size()
        player1_x, player1_y = player1.get_current_tile()
        player2_x, player2_y = player2.get_current_tile()

        for _ in range(self.n_destruction_blocks):
            block_x, block_y = self.__generate_cordinate()
            if (player1_x == block_x or player2_x == block_x):
                block_x, block_y = self.__generate_cordinate()
            if (player1_y == block_y or player2_y == block_y):
                block_x, block_y = self.__generate_cordinate()

            for wall in self.collision_rect:
                if wall.collidepoint(block_x, block_y):
                    block_x, block_y = self.__generate_cordinate()

            destruction_block = DestructionBlock(block_x, block_y, tile_size, tile_size)
            self.destruction_blocks.append(destruction_block)

    def __process_destrucion_blocks(self, entity: Entity, destruction_blocks):
        for destruction_block in destruction_blocks:
            if destruction_block.is_alive:
                entity.collision_entity([destruction_block])

    def custom_collision(self, entity: Entity):
        concurrancy_for_each(self.__process_destrucion_blocks, self.destruction_blocks, entity)
