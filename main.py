import os
import pyxel
import random

import me
import item
import score

class App:
    def __init__(self):
        pyxel.init(128, 128, caption="Snake Game", fps=5)
        pyxel.load(os.path.dirname(os.path.abspath(__file__)) + "/assets.pyxel")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.item.update()
        self.me.update()

        if self.item.x == self.me.x and self.item.y == self.me.y:
            self.eat()

    def draw(self):
        pyxel.cls(0)

        self.me.draw()
        self.item.draw()
        self.score.draw()

    def eat(self):
        self.item.alives = False
        self.score.point += 1
        self.me.ghosts += 1

    me = me.Me()
    item = item.Item()
    score = score.Score()

App()
