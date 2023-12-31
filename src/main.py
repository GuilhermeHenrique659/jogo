from bomber.screen.gameOverScreen import GameOverScreen
from bomber.screen.gameScreen import GameScreen
from bomber.screen.historyScreen import HistoryScreen
from bomber.screen.menuScreen import MenuScreen
from common.Game import Game
from common.config import Config

class Bomber(Game):
    def __init__(self, name: str, width: int, height: int, tile_size = None,  debug_mode = None):
        super().__init__(name, width, height, tile_size, debug_mode)
    
    def setup(self):
        self.fps = 60
        self.game = GameScreen()
        self.gameOver = GameOverScreen(self.set_current_screen_to_game)
        self.current_screen =  MenuScreen(self.set_current_screen_to_history)
        self.history = HistoryScreen(self.set_current_screen_to_game)

    def game_over(self):
        if self.game.player1.is_alive and self.game.player2.is_alive: return
        
        del self.game
        self.current_screen = self.gameOver
        self.game = GameScreen()

    def set_current_screen_to_game(self):
        del self.current_screen
        self.current_screen = self.game

    def set_current_screen_to_history(self):
        del self.current_screen
        self.current_screen = self.history

    def main(self):
        self.display.fill("purple")
        self.game_over()
        self.current_screen.render()


WIDTH, HEIGHT = Config.display_size()
Bomber = Bomber('Bomber man', WIDTH, HEIGHT, Config.tile_size(), True)
Bomber.render()