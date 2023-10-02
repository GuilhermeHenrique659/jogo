
from pygame.key import ScancodeWrapper
from common.Entity import Entity
from common.sprite import Sprite


class LifeIcon(Entity):
    def setup(self):
        self.current_sprite = Sprite(['assets/player/bomber (15).png'])

    def loop(self, keys: ScancodeWrapper, *args):
        return super().loop(keys, *args)