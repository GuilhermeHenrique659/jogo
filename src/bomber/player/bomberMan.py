import time
import pygame
from pygame.key import ScancodeWrapper
from bomber.bomb.Bomb import Bomb
from bomber.enums.playersKeys import PlayerOneKey, PlayerTwoKey
from bomber.observer.bomb.observer import observer
from bomber.observer.bomb.playerSubject import PlayerSubject
from common.Entity import Entity
from common.sprite import Sprite


PLAYER_TYPES = [1, 2]

class BomberMan(Entity):
    def __init__(self, x: int, y: int, width: int = None, height: int = None, use_limit: bool = None, gravity_force: float = None, player_type = 1) -> None:
        if player_type not in PLAYER_TYPES: raise ValueError(f"player_type deve ser {PLAYER_TYPES}")
        self.player_type = player_type
        self.bomb = None
        self.num_bomb = 3
        self.bomb_start_time = 0
        self.life = 2
        self.dying_time = 0
        self.subject = PlayerSubject(self)
        observer.attach(self.subject)
        super().__init__(x, y, width, height, use_limit, gravity_force)

    def setup(self):
        self.walk_horizotal = Sprite([
            'assets/player/07_NeoEarlyBomberman.png', 
            'assets/player/08_NeoEarlyBomberman.png', 
            'assets/player/09_NeoEarlyBomberman.png', 
            'assets/player/10_NeoEarlyBomberman.png', 
            'assets/player/11_NeoEarlyBomberman.png',
            'assets/player/12_NeoEarlyBomberman.png',
            'assets/player/13_NeoEarlyBomberman.png',
             ])
        self.walk_up = Sprite([
            'assets/player/00_NeoEarlyBomberman.png', 
            'assets/player/01_NeoEarlyBomberman.png', 
            'assets/player/02_NeoEarlyBomberman.png', 
            'assets/player/03_NeoEarlyBomberman.png', 
            'assets/player/04_NeoEarlyBomberman.png',
            'assets/player/05_NeoEarlyBomberman.png',
            'assets/player/06_NeoEarlyBomberman.png',
             ])
        
        self.dying = Sprite([
            'assets/player/dead1 (1).png',
            'assets/player/dead1 (2).png', 
            'assets/player/dead1 (3).png', 
            'assets/player/dead1 (4).png', 
            'assets/player/dead1 (5).png', 
            'assets/player/dead1 (6).png',
        ])
        
        self.walk_down = Sprite([
            'assets/player/14_NeoEarlyBomberman.png', 
            'assets/player/15_NeoEarlyBomberman.png',
            'assets/player/16_NeoEarlyBomberman.png',
            'assets/player/17_NeoEarlyBomberman.png',
            'assets/player/18_NeoEarlyBomberman.png',
            'assets/player/19_NeoEarlyBomberman.png',
            'assets/player/20_NeoEarlyBomberman.png',
        ])
        self.idle = Sprite(['assets/player/18_NeoEarlyBomberman.png'])
        self.current_sprite = self.dying

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
        self.dying_time += 1
        self.current_sprite = self.dying
        self.kill()

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
        
        if self.life == 0:
            self.die()
        self.bomb_reload()