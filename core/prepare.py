import pygame
import sys
CAPTION = "Snake Eater"
WINSIZE = (720,480)


check_errors = pygame.init()
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')


# Initialise game window
pygame.display.set_caption(CAPTION)
game_window = pygame.display.set_mode(WINSIZE)


# FPS (frames per second) controller
clock = pygame.time.Clock()