import pygame
from enum import Enum

class PlayerOneKey(Enum):
    LEFT = pygame.K_a
    RIGHT =  pygame.K_d
    UP = pygame.K_w
    DOWN = pygame.K_s
    BOMB = pygame.K_SPACE

class PlayerTwoKey(Enum):
    LEFT = pygame.K_LEFT
    RIGHT =  pygame.K_RIGHT
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    BOMB = pygame.K_RCTRL