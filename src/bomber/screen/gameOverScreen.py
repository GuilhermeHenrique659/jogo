import pygame
from common.point import Point
from common.screen import Screen
from common.text import Text


class GameOverScreen(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.init_text = Text('Reniciar jogo: Aperte Enter', 'red', 32, Point((144, 576)))
        self.quit_text = Text('Sair jogo: Aperte ESC', 'red', 32, Point((144, 624)))
        self.current_select = self.init_text

    def render(self):
        self.cover_screen_with_image('assets/FrY6_BPWcAgG-xp.png')
        self.init_text.render(self.display)
        self.quit_text.render(self.display)

