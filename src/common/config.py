
import pygame


class Config:
    @staticmethod
    def display_size():
        return 1248, 768

    @staticmethod
    def tile_size():
        return 48
    
    @staticmethod
    def font():
        return pygame.font.get_default_font()