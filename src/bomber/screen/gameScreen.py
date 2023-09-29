
from bomber.icons.bombIcon import BombIcon
from bomber.maps.base_map import BaseMap
from bomber.player.bomberMan import BomberMan
from common.screen import Screen


class GameScreen(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.player1 = BomberMan(150, 150, player_type=1)
        self.player2 = BomberMan(800, 600, player_type=2)
        self.bomb_icons_player_1 = []
        self.bomb_icons_player_2 = []
        self.map = BaseMap('assets/map.tmx', { 'wall_l': 2684354561, 'wall_t': 3221225473, 'wall_b': 1, 'wall_r': 1610612737, })
        self.map.generate_destruction_blocks(self.player1, self.player2)

    def reset(self):
        self.player1.life = 2
        self.player1.is_alive = True
        self.player2.life = 2
        self.player2.is_alive = True
        self.map.generate_destruction_blocks(self.player1, self.player2)

    def set_player2_bomb_icons(self, num_bombs: int):
        if len(self.bomb_icons_player_2) > 3: return
    
        self.bomb_icons_player_2 = []
        for i in range(num_bombs):
            self.bomb_icons_player_2.append(BombIcon(1000 + i * 48, 10))

    def set_player1_bomb_icons(self, num_bombs: int):
        if len(self.bomb_icons_player_1) > 3: return
        self.bomb_icons_player_1 = []
        for i in range(num_bombs):
            self.bomb_icons_player_1.append(BombIcon(32 + i * 48, 10))

            
    def render_bomb_icons(self):
        for icon in self.bomb_icons_player_1:
            icon.render()
        for icon in self.bomb_icons_player_2:
            icon.render()

    def render(self):
        self.map.render()
        self.map.render_destruction_blocks()
        self.set_player1_bomb_icons(self.player1.num_bomb)
        self.player1.render()
        self.player2.render()
        self.set_player2_bomb_icons(self.player2.num_bomb)
        self.render_bomb_icons()
        self.player1.collision_entity([self.player2, *self.player1.entities, *self.player2.entities])
        self.player2.collision_entity([self.player1, *self.player1.entities, *self.player2.entities])
        self.map.collision_map_with_entity(self.player1)
        self.map.collision_map_with_entity(self.player2)
