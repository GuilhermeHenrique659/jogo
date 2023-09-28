
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.sprite import Sprite


class BombIcon(Entity):
    def setup(self):
        self.current_sprite = Sprite([
        'assets/bomb/00_bomb.png', 
        'assets/bomb/01_bomb.png', 
        'assets/bomb/02_bomb.png', 
        'assets/bomb/03_bomb.png', 
        'assets/bomb/04_bomb.png',
        'assets/bomb/05_bomb.png'
        ], tick=1000)
    
    def loop(self, keys: ScancodeWrapper, *args):
        pass