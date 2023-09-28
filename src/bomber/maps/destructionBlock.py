
from pygame.key import ScancodeWrapper
from bomber.observer.bomb.blockSubject import BlockSubject
from bomber.observer.bomb.observer import observer
from common.Entity import Entity


class DestructionBlock(Entity):
    def setup(self):
        self.subject = BlockSubject(self)
        observer.attach(self.subject)

    
    def loop(self, keys: ScancodeWrapper, *args):
        pass