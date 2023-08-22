
from abc import ABC, abstractmethod
import pygame
from pygame import Surface
from pygame.time import Clock

class Game(ABC):
    __name: str
    width: int
    height: int
    display: Surface
    clock: Clock
    loop = True
    fps = 60

    def __init__(self, name: str, width: int, height: int) -> None:
        self.__name = name
        self.width = width
        self.height = height

        self.__init()
        self.__init_diplay()
        super().__init__()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def main(self):
        pass

    def render(self):
        self.setup()
        while self.loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False

            self.main()

            pygame.display.flip()
            self.clock.tick(self.fps)
                

    def __init(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
    
    def __init_diplay(self):
        pygame.display.set_caption(self.__name)
        self.display = pygame.display.set_mode((self.width, self.height))

