import pygame
from themes.normal import *


class GameOverText:
    def __init__(self, game_window, frame_size):
        self.game_window = game_window
        self.frame_size = frame_size
        self.game_over()

    def draw(self, surf):
        surf.fill(black)
        surf.blit(self.game_over_surface, self.game_over_rect)

    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 90)
        self.game_over_surface = my_font.render('YOU DIED', True, red)
        self.game_over_rect = self.game_over_surface.get_rect()
        self.game_over_rect.midtop = (self.frame_size[0]/2, self.frame_size[1]/4)

class ScoreText:
    def __init__(self, game_window, frame_size):
        self.game_window = game_window
        self.frame_size = frame_size

    def draw(self, choice, surf, size, color, score):
        score_font = pygame.font.SysFont('times new roman', size)
        self.score_surface = score_font.render('Score : ' + str(score), True, color)
        self.score_rect = self.score_surface.get_rect()

        if choice == 1:
            self.score_rect.midtop = (self.frame_size[0]/10, 15)
        else:
            self.score_rect.midtop = (self.frame_size[0]/2, self.frame_size[1]/1.25)

        self.game_window.blit(self.score_surface, self.score_rect)

        