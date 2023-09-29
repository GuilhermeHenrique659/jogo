import pygame
from bomber.screen.gameOverScreen import GameOverScreen
from bomber.screen.gameScreen import GameScreen
from bomber.screen.menuScreen import MenuScreen
from common.Game import Game
from common.config import Config

class Bomber(Game):
    def __init__(self, name: str, width: int, height: int, tile_size = None,  debug_mode = None):
        super().__init__(name, width, height, tile_size, debug_mode)
    
    def setup(self):
        self.fps = 60
        self.game = GameScreen()
        self.gameOver = GameOverScreen(self.set_current_screen_game)
        self.current_screen =  MenuScreen(self.set_current_screen_game)

    def game_over(self):
        if self.game.player1.is_alive and self.game.player2.is_alive: return
        
        self.game.reset()
        self.current_screen = self.gameOver

    def set_current_screen_game(self):
        self.current_screen = self.game

    def main(self):
        self.display.fill("purple")
        self.game_over()
        self.current_screen.render()


WIDTH, HEIGHT = Config.display_size()
Bomber = Bomber('Arabe simulator', WIDTH, HEIGHT, Config.tile_size(), True)
Bomber.render()