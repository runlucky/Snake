import random
import pyxel

class Item:
    x = 0
    y = 0

    alives = False

    def update(self):
        if self.alives:
            return

        if random.randrange(10) == 0:
            self.alives = True
            self.x = random.randrange(16)
            self.y = random.randrange(16)


    def draw(self):
        if self.alives:
            pyxel.blt(self.x * 8, self.y * 8, 0, 8, 0, 8, 8)


