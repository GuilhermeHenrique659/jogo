
from abc import ABC, abstractclassmethod

import pygame

from common.config import Config


class Screen(ABC):
    def __init__(self, bg: str = None) -> None:
        self.display = pygame.display.get_surface()
        self.bg = bg
        self.setup()
        super().__init__()

    def setup(self):
        if not self.bg: return
        w, h = Config.display_size()
        image = pygame.image.load(self.bg).convert()
        self.image_bg = pygame.transform.scale(image, (w, h))

    def cover_screen_with_image(self):
        self.display.blit(self.image_bg, (0, 0))


    @abstractclassmethod
    def render(self, *args):
        pass