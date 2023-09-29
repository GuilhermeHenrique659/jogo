import time
from typing import Tuple
from pygame.key import ScancodeWrapper
from bomber.bomb.bombFragment import BombFragment
from bomber.observer.bomb.observer import observer
from common.Entity import Entity
from common.config import Config
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
        
        self.bomb_fragments = []
        self.fragments_duration = 0 

        
    def explode(self):
        observer.notify(self)

    def get_point(self, direction: str) -> Tuple[int, int]:
        tile_size = Config.tile_size()
        bomb_x, bomb_y = self.get_current_tile()
        
        bomb_tile_x = bomb_x // tile_size
        bomb_tile_y = bomb_y // tile_size

        if direction == 'UP':
            return (bomb_tile_x) * tile_size, (bomb_tile_y - 1) * tile_size
        
        elif direction == 'DOWN':
            return (bomb_tile_x) * tile_size, (bomb_tile_y + 1) * tile_size
        
        elif direction == 'LEFT':
            return (bomb_tile_x - 1) * tile_size, (bomb_tile_y) * tile_size
        
        elif direction == 'RIGHT':
            return (bomb_tile_x + 1) * tile_size, (bomb_tile_y) * tile_size

            

    def generate_fragment(self):
        points = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        for point in points:
            x, y = self.get_point(point)
            self.bomb_fragments.append(BombFragment(x, y))
        self.render_fragment()

    def render_fragment(self):
        for fragment in self.bomb_fragments:
            fragment.render()
        
    def loop(self, keys: ScancodeWrapper):
        current_time = time.time()
        if current_time - self.start_time >= 3:
            
            self.generate_fragment()
            self.fragments_duration += 1
            if self.fragments_duration >= 40:
                self.explode()
                self.kill()


        