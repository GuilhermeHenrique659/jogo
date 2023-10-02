import time
import pygame
from pygame.key import ScancodeWrapper
from bomber.bomb.Bomb import Bomb
from bomber.enums.playersKeys import PlayerOneKey, PlayerTwoKey
from bomber.icons.bombIcon import BombIcon
from bomber.icons.lifeIcon import LifeIcon
from bomber.observer.bomb.subject import subject
from bomber.observer.bomb.playerObserver import PlayerObserver
from common.Entity import Entity
from common.config import Config
from common.sprite import Sprite
from common.point import Point

PLAYER_TYPES = [1, 2]

class BomberMan(Entity):
    def __init__(self, x: int, y: int, width: int = None, height: int = None, use_limit: bool = None, gravity_force: float = None, player_type = 1) -> None:
        if player_type not in PLAYER_TYPES: raise ValueError(f"player_type deve ser {PLAYER_TYPES}")
        self.player_type = player_type
        super().__init__(x, y, width, height, use_limit, gravity_force)

    def setup(self):
        self.bomb = None
        self.num_bomb = 3
        self.bomb_start_time = 0
        self.life = 2
        self.dying_tick = 0
        self.subject = PlayerObserver(self)
        
        subject.attach(self.subject)

        self.walk_horizotal = Sprite([
            'assets/player/bomber (12).png',
            'assets/player/bomber (13).png',
            'assets/player/bomber (14).png',
            ])
        self.walk_up = Sprite([
            'assets/player/bomber (3).png',
            'assets/player/bomber (4).png',
            'assets/player/bomber (5).png',
             ])
        
        self.dying = Sprite([
            'assets/player/bomber (6).png',
            'assets/player/bomber (7).png',
            'assets/player/bomber (8).png',
            'assets/player/bomber (9).png',
            'assets/player/bomber (10).png',
            'assets/player/bomber (11).png',
        ])
        
        self.walk_down = Sprite([
            'assets/player/bomber (15).png',
            'assets/player/bomber (1).png',
            'assets/player/bomber (2).png',
        ])
        self.idle = Sprite(['assets/player/bomber (15).png'])
        self.current_sprite = self.dying

    def life_icons(self):
        x, y = Point((1 if self.player_type == 1 else 22, 15)).convert_to_point().get_points()
        return [LifeIcon(x + i * Config.tile_size(), y) for i in range(self.life)]

    def bomb_icons(self):
        x, y = Point((1 if self.player_type == 1 else 22, 0)).convert_to_point().get_points()
        return [BombIcon(x + i * Config.tile_size(), y) for i in range(self.num_bomb)]

    def get_key(self, command: str):
        if self.player_type == 1:
            return PlayerOneKey[command].value
        elif self.player_type == 2:
            return PlayerTwoKey[command].value

    def bomb_hit(self):
        self.life -= 1 

    def bomb_reload(self):
        if self.num_bomb >= 3: return
        current_time = time.time()

        if current_time - self.bomb_start_time > 2:
            self.num_bomb += 1

    def put_bomb(self):
        current_time = time.time()
        if current_time - self.bomb_start_time <= 1: return
        x, y = self.get_current_tile()
        for entity in self.entities:
            if entity.rect.x == x and entity.rect.y == y: return

        self.bomb = Bomb(x, y)
        self.num_bomb -= 1
        self.bomb_start_time = time.time()
        self.entities.append(self.bomb)


    def die(self):     
        self.dying_tick += 1
        self.current_sprite = self.dying
        if self.dying_tick >= 60:
            self.kill()
            self.dying_tick = 0

    def loop(self, keys: ScancodeWrapper):
        if (keys[self.get_key('RIGHT')]):
            self.velocity.x = 3
            if self.walk_horizotal.is_fliped:
                self.walk_horizotal.flip(True)
            self.current_sprite = self.walk_horizotal
        elif keys[self.get_key('LEFT')]:
            self.velocity.x = -3
            if not self.walk_horizotal.is_fliped:
                self.walk_horizotal.flip(True)
            self.current_sprite = self.walk_horizotal
        elif keys[self.get_key('UP')]:
            self.current_sprite = self.walk_up
            self.velocity.y = -3
        elif keys[self.get_key('DOWN')]:
            self.current_sprite = self.walk_down
            self.velocity.y = 3
    
        else:
            self.velocity.x = 0
            self.velocity.y = 0
            self.current_sprite = self.idle

        if keys[self.get_key('BOMB')] and self.num_bomb > 0:
            self.put_bomb()
        
        if self.life <= 0:
            self.die()
        self.bomb_reload()