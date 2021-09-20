import pygame as pygame
from .element import Element

class Snake(Element):
    def __init__(self):
        super().__init__(100, 50)
        self.body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0

    def update(self, food):
        self._move(self.direction)
        self._grow(food)

        
    def _move(self, direction):
        if direction == 'UP':
            self.y -= 10
        if direction == 'DOWN':
            self.y += 10
        if direction == 'LEFT':
            self.x -= 10
        if direction == 'RIGHT':
            self.x += 10
        
    def _grow(self, food):
        self.body.insert(0, list(self.position))
        if self.collision(food):
            self.score += 1
            food.eat()
        else:
            self.body.pop()

    def body_collision(self):
        for block in self.body[1:]:
            return self.x == block[0] and self.y == block[1]
    
    def border_collision(self, frame_size_x, frame_size_y):
        if self.x < 0 or self.x > frame_size_x-10:
            return True
        if self.y < 0 or self.y > frame_size_y-10:
            return True
        return False

    def set_change(self, event):

        # W -> Up; S -> Down; A -> Left; D -> Right
        if event.key == pygame.K_UP or event.key == ord('w'):
            self.change_to = 'UP'
        if event.key == pygame.K_DOWN or event.key == ord('s'):
            self.change_to = 'DOWN'
        if event.key == pygame.K_LEFT or event.key == ord('a'):
            self.change_to = 'LEFT'
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            self.change_to = 'RIGHT'
        # Esc -> Create event to quit the game
        if event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        
    def set_direction(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'