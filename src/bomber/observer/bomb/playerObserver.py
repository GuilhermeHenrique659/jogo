from bomber.bomb.Bomb import Bomb
from common.Entity import Entity
from common.config import Config

class PlayerObserver:
    def __init__(self, player: Entity) -> None:
        self.player = player

    def update(self, bomb: Bomb):
        tile_size = Config.tile_size()
        block_x, block_y = self.player.get_current_tile()
        bomb_x, bomb_y = bomb.get_current_tile()

        block_tile_x = block_x // tile_size
        bomb_tile_x = bomb_x // tile_size
        
        block_tile_y = block_y // tile_size
        bomb_tile_y = bomb_y // tile_size

        if (abs(bomb_tile_x - block_tile_x) <= 1 and bomb_tile_y == block_tile_y) or \
            (abs(bomb_tile_y - block_tile_y) <= 1 and bomb_tile_x == block_tile_x):
                self.player.bomb_hit()