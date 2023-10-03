from bomber.screen.cursor import Cursor
from common.point import Point
from common.screen import Screen
from common.text import Text

class HistoryScreen(Screen):
    def __init__(self, action) -> None:
        super().__init__()
        self.history_text_1 = Text('Durante a união sovietica, familares acusada de atos anti sovientico', 'black', 32, Point((2, 5)).convert_to_point())    
        self.history_text_2 = Text('eram jogadas no gulag, onde seus primogenito lutam com bombas,', 'black', 32, Point((2, 6)).convert_to_point())
        self.history_text_3 = Text('para que decida quem irá ter acesso a comida.', 'black', 32, Point((2, 7)).convert_to_point())
        self.init_text = Text('Proximo', 'black', 32, Point((3, 12)).convert_to_point())
        self.cursor = Cursor(Point((2, 12)).convert_to_point(), [12])
        self.action = action


    def render(self):
        self.cover_screen_with_image('assets/historyBg.png')
        self.history_text_1.render(self.display)
        self.history_text_2.render(self.display)
        self.history_text_3.render(self.display)
        self.init_text.render(self.display)
        self.cursor.render()
        if self.cursor.point.compare_tile_y(12) and self.cursor.confirm:
            self.action()
            self.cursor.reset()