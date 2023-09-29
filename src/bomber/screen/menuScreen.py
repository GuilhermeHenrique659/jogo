
import pygame
from common.point import Point
from common.screen import Screen
from common.text import Text


class MenuScreen(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.init_text = Text('Iniciar jogo: Aperte Enter', 'white', 32, Point((144, 576)))
        self.quit_text = Text('Sair jogo: Aperte ESC', 'white', 32, Point((144, 624)))
        self.current_select = self.init_text

    def render(self):
        self.display.fill("purple")
        self.init_text.render(self.display)
        self.quit_text.render(self.display)

