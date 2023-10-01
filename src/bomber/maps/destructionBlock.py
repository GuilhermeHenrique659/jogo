
from pygame.key import ScancodeWrapper
from bomber.observer.bomb.blockSubject import BlockSubject
from bomber.observer.bomb.observer import observer
from common.Entity import Entity
from common.sprite import Sprite


class DestructionBlock(Entity):
    def setup(self):
        self.current_sprite = Sprite(['assets/tile70.png'])
        self.current_sprite.scale_tile()
        self.subject = BlockSubject(self)
        observer.attach(self.subject)

    
    def loop(self, keys: ScancodeWrapper, *args):
        pass