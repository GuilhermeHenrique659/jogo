
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.sprite import Sprite


class BombIcon(Entity):
    def setup(self):
        self.current_sprite = Sprite([
            'assets/bomb/bomb (5).png', 
            'assets/bomb/bomb (4).png', 
            'assets/bomb/bomb (3).png', 
        ], tick=300)
    
    def loop(self, keys: ScancodeWrapper, *args):
        pass