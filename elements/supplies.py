import random
from .element import Element

frame_size_x = 720 
frame_size_y = 480

class Pellet(Element):

    def __init__(self):
        super().__init__(
            random.randrange(1, (frame_size_x//10)) * 10, 
            random.randrange(1, (frame_size_y//10)) * 10
            )
        self.active = True

    def eat(self):
        self.active = False