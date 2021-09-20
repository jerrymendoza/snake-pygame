import pygame as pygame
from .element import Element

class Snake(Element):
    def __init__(self):
        super().__init__(100, 50)
        self.body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

    def update(self, direction, food, score):
        self._move(direction)
        return self._grow(food, score)

        
    def _move(self, direction):
        if direction == 'UP':
            self.y -= 10
        if direction == 'DOWN':
            self.y += 10
        if direction == 'LEFT':
            self.x -= 10
        if direction == 'RIGHT':
            self.x += 10
        
    def _grow(self, food, score):
        self.body.insert(0, list(self.position))
        if self.collision(food):
            score += 1
            food.eat()
        else:
            self.body.pop()
        return score