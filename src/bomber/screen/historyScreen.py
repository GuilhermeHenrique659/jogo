from bomber.screen.cursor import Cursor
from common.point import Point
from common.screen import Screen
from common.text import Text

class HistoryScreen(Screen):
    def __init__(self, action) -> None:
        super().__init__('assets/historyBg.png')
        self.history_text = [
            'Em um futuro distópico, o mundo está mergulhado em caos e anarquia.',
            'As nações caíram, e o que restou da ',
            'União Soviética é um território devastado pela guerra e pela radiação.',
            'Duas famílias, os Volkov e os Ivanov, emergem',
            'como as últimas esperanças de sobrevivência  em meio ao deserto destruído.'
        ]
        self.init_text = Text('Proximo', 'white', 32, Point((3, 12)).convert_to_point())
        self.cursor = Cursor(Point((2, 12)).convert_to_point(), [12])
        self.action = action


    def render(self):
        self.cover_screen_with_image()
        for index, text in enumerate(self.history_text):
            Text(text, 'white', 24, Point((3, 4 + index)).convert_to_point()).render(self.display)
        self.init_text.render(self.display)
        self.cursor.render()
        if self.cursor.point.compare_tile_y(12) and self.cursor.confirm:
            self.action()
            self.cursor.reset()