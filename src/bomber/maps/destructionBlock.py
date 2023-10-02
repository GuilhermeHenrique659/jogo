
from pygame.key import ScancodeWrapper
from bomber.observer.bomb.blockObserver import BlockObserver
from bomber.observer.bomb.subject import subject
from common.Entity import Entity
from common.sprite import Sprite


class DestructionBlock(Entity):
    def setup(self):
        self.current_sprite = Sprite(['assets/tile70.png'])
        self.current_sprite.scale_tile()
        self.subject = BlockObserver(self)
        subject.attach(self.subject)

    
    def loop(self, keys: ScancodeWrapper, *args):
        pass