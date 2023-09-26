
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

    def __init__(self, name: str, width: int, height: int, tile_size = None, debug_mode = False) -> None:
        self.__name = name
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.debug_mode = debug_mode

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
                if self.debug_mode:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        tile_x = mouse_x // self.tile_size
                        tile_y = mouse_y // self.tile_size
                        print(f"Tile address: ({tile_x}, {tile_y}) \nTile coordinate: ({tile_x * self.tile_size}, {tile_y * self.tile_size})")

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

