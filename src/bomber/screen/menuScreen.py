
import sys
from typing import Callable
import pygame
from bomber.screen.cursor import Cursor
from common.music import MusicPlayer
from common.point import Point
from common.screen import Screen
from common.text import Text


class MenuScreen(Screen):
    def __init__(self, action: Callable) -> None:
        super().__init__()
        self.init_text = Text('Iniciar jogo', 'white', 32, Point((3, 12)).convert_to_point())
        self.quit_text = Text('Sair jogo', 'white', 32, Point((3, 13)).convert_to_point())
        self.music = MusicPlayer()
        self.music.play_music('assets/game.mp3')
        self.cursor = Cursor(Point((2, 12)).convert_to_point(), [12, 13])
        self.action = action

    def shutdown(self):
        pygame.quit()
        sys.exit()

    def render(self):
        self.display.fill("purple")
        self.init_text.render(self.display)
        self.quit_text.render(self.display)
        self.cursor.render()
        if self.cursor.point.compare_tile_y(12) and self.cursor.confirm:
            self.action()
            self.music.stop_music()
            self.cursor.reset()
        if self.cursor.point.compare_tile_y(13) and self.cursor.confirm:
            self.shutdown()
            self.cursor.reset()


