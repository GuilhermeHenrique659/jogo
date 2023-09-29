
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.sprite import Sprite


class BombFragment(Entity):
    def __init__(self, x: int, y: int, width: int = None, height: int = None, use_limit: bool = None, gravity_force: float = None) -> None:
        self.duration_time = 0
        super().__init__(x, y, width, height, use_limit, gravity_force)

    def setup(self):
        self.current_sprite = Sprite(['assets/bomb/03_bomb.png',
                                      'assets/bomb/04_bomb.png',
                                      'assets/bomb/05_bomb.png'], 300)

    
    def loop(self, keys: ScancodeWrapper, *args):
        self.duration_time += 1
        if self.duration_time == 30:
            self.kill()