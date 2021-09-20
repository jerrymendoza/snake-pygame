
class Element:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def position(self):
        return [self.x, self.y]

    def collision(self, element):
        if self.position == element.position:
            return True
        return False