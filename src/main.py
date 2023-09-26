import pygame
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.Game import Game
from common.config import Config
from common.map import Map
from common.sprite import Sprite

class Teste(Entity):
    def setup(self):
        self.walk = Sprite(['assets/player/walk_1.png', 'assets/player/walk_2.png', 'assets/player/walk_3.png'])
        self.idle = Sprite(['assets/player/idle_1.png', 'assets/player/idle_2.png'])
        self.current_sprite = self.idle

    def loop(self, keys: ScancodeWrapper):
        if (keys[pygame.K_d]):
            self.x += 5
            self.current_sprite = self.walk
        elif keys[pygame.K_a]:
            self.x -= 5
            self.current_sprite = self.walk

        else:
            self.current_sprite = self.idle


class Bar(Game):
    def __init__(self, name: str, width: int, height: int, tile_size = None,  debug_mode = None):
        super().__init__(name, width, height, tile_size, debug_mode)
    
    def setup(self):
        self.fps = 60
        self.player = Teste(0, 0, use_limit=True)
        self.map = Map('assets/map.tmx', { 'tile': 81 })

    def main(self):
        self.display.fill("purple")
        self.map.render()
        self.player.render()
        self.map.collision_map_with_entity(self.player)

WIDTH, HEIGHT = Config.display_size()
bar = Bar('Bar simulator', WIDTH, HEIGHT, Config.tile_size(), True)
bar.render()