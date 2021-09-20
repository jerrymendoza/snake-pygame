import pygame
import sys
import time
from themes.normal import *

class Pencil:
    def __init__(self, game_window):
        self.game_window = game_window

    def draw(self, element, color):
        if isinstance(element, list):
            for e in element:
                self._draw(e, color)
        else:
            self._draw(element.position, color)

    
    def _draw(self, pos, color):
        pygame.draw.rect(
            self.game_window, color,
            pygame.Rect(*pos, 10, 10))
