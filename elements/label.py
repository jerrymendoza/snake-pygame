import pygame
from themes.normal import *


class GameOverText:
    def __init__(self, game_windows, frame_size):
        self.game_windows = game_windows
        self.frame_size = frame_size
        self.game_over()

    def draw(self,surf):
        surf.fill(black)
        surf.blit(self.game_over_surface, self.game_over_rect)

    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 90)
        self.game_over_surface = my_font.render('YOU DIED', True, red)
        self.game_over_rect = self.game_over_surface.get_rect()
        self.game_over_rect.midtop = (self.frame_size[0]/2, self.frame_size[1]/4)
