
from pygame import Surface
import pygame
from common.config import Config

from common.point import Point


class Text:
    def __init__(self, text: str, color: str, size: int, point: Point) -> None:
        self.content = text
        font = pygame.font.Font(Config.font(), size)
        self.text_surface = font.render(text, True, color)
        self.point = point


    def render(self, display: Surface):
        display.blit(self.text_surface, self.point.get_points())