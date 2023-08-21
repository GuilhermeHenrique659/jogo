from common.Game import Game

class Bar(Game):
    def __init__(self, name: str, width: int, height: int):
        super().__init__(name, width, height)
    
    def main(self):
        self.display.fill("purple")


bar = Bar('Bar simulator', 1280, 720)
bar.render()