
from abc import ABC, abstractclassmethod

import pygame

from common.config import Config


class Screen(ABC):
    def __init__(self) -> None:
        self.display = pygame.display.get_surface()
        super().__init__()

    def cover_screen_with_image(self, src: str):
        w, h = Config.display_size()
        image = pygame.image.load(src).convert()
        image = pygame.transform.scale(image, (w, h))
        self.display.blit(image, (0, 0))


    @abstractclassmethod
    def render(self, *args):
        pass