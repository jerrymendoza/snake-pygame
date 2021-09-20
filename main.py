"""
Snake Eater
Made with PyGame
"""

import pygame, sys
from elements import player, supplies, label
from core import tools, prepare
from themes.normal import *

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 25

game_over_label = label.GameOverText(prepare.game_window, prepare.WINSIZE)
score_label = label.ScoreText(prepare.game_window, prepare.WINSIZE)
# Game variables
snake = player.Snake()
food = supplies.Pellet()
pencil = tools.Pencil(prepare.game_window)

# Main logic
while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
           snake.set_change(event)

    # Making sure the snake cannot move in the opposite direction instantaneously
    snake.set_direction()

    # Moving the snake and grow
    snake.update(food)

    # Spawning food on the screen
    if not food.active:
        food = supplies.Pellet()

    # GFX
    prepare.game_window.fill(black)

    # Snake body
    pencil.draw(snake.body, green)

    # Snake food
    pencil.draw(food, white)

    # Game Over conditions
    if snake.body_collision() or snake.border_collision(*prepare.WINSIZE):
        game_over_label.draw(prepare.game_window)

    score_label.draw(1, prepare.game_window, 20, white, snake.score)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    prepare.clock.tick(difficulty)