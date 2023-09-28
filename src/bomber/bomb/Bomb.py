import threading
import time

from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.sprite import Sprite

class Bomb(Entity):
    def setup(self):
        self.start_time = time.time()
        self.current_sprite = Sprite([
            'assets/bomb/00_bomb.png', 
            'assets/bomb/01_bomb.png', 
            'assets/bomb/02_bomb.png', 
            'assets/bomb/03_bomb.png', 
            'assets/bomb/04_bomb.png',
            'assets/bomb/05_bomb.png'
            ], tick=1000)

        
    def explode(self):
        self.kill()
        
    def loop(self, keys: ScancodeWrapper):
        current_time = time.time()
        if current_time - self.start_time >= 3:
            self.explode()