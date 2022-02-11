#Imports gameobject class from gameobject.py
from gameObject import GameObject

# creates enemy class using gameobject class as a base
class Enemy(GameObject):

    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        self.speed = speed

    def move(self, max_width):
        if self.x <= 0:
            self.speed = abs(self.speed)
        elif self.x >= max_width - self.width:
            self.speed = -self.speed

        self.x += self.speed