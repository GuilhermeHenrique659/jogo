from bomber.icons.bombIcon import BombIcon
from bomber.maps.base_map import BaseMap
from bomber.player.bomberMan import BomberMan
from common.concurrancyForEach import concurrancy_for_each
from common.config import Config
from common.music import MusicPlayer
from common.screen import Screen
import threading

class GameScreen(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.player1 = BomberMan(150, 150, player_type=1)
        self.player2 = BomberMan(800, 600, player_type=2)
        self.bomb_icons_player_1 = []
        self.bomb_icons_player_2 = []
        self.map = BaseMap('assets/map.tmx', { 
                                    'wall_l': 2684354561,
                                    'wall_t': 3221225473, 
                                    'wall_b': 1, 
                                    'wall_r': 1610612737, 
                                            })
        self.map.generate_destruction_blocks(self.player1, self.player2)
        self.map.setup_map()

    def reset(self):
        self.player1 = BomberMan(150, 150, player_type=1)
        self.player2 = BomberMan(800, 600, player_type=2)
        self.map.generate_destruction_blocks(self.player1, self.player2)

    def render_bomb_icons(self):
        for icon in self.player1.bomb_icons():
            icon.render()
        for icon in self.player2.bomb_icons():
            icon.render()

    def render_file(self):
        for icon in self.player1.life_icons():
            icon.render()
        for icon in self.player2.life_icons():
            icon.render()

    def render(self):
        concurrancy_for_each(self.map.render, self.map.map_imgs)
        concurrancy_for_each(self.map.render_destruction_blocks, self.map.destruction_blocks)
        self.render_file()

        player1_thread = threading.Thread(target=self.player1.render)
        player1_thread.start()
        player2_thread = threading.Thread(target=self.player2.render)
        player2_thread.start()

        self.render_bomb_icons()

        collision_thread_player1_enities = threading.Thread(target= self.player1.collision_entity, args=([self.player2, *self.player1.entities, *self.player2.entities],))
        collision_thread_player1_enities.start()
        collision_thread_player2_enities = threading.Thread(target= self.player2.collision_entity, args=([self.player1, *self.player1.entities, *self.player2.entities],))
        collision_thread_player2_enities.start()

        collision_thread_map_player1 = threading.Thread(target=self.map.collision_map_with_entity, args=(self.player1,))
        collision_thread_map_player1.start()
        collision_thread_map_player2 = threading.Thread(target=self.map.collision_map_with_entity, args=(self.player2,))
        collision_thread_map_player2.start()
