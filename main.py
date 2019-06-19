import os
import pyxel
import random

import me



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
            self.item.alives = False


    def draw(self):
        pyxel.cls(0)

        # blt(x, y, img, u, v, w, h, [colkey])
        #イメージバンクimg(0-2) の (u, v) からサイズ (w, h) の領域を (x, y) にコピーする。
        # w、hそれぞれに負の値を設定すると水平、垂直方向に反転する。colkeyに色を指定すると透明色として扱われる

        self.me.draw()
        self.item.draw()

    def draw_ghost(self, x, y):
        pyxel.blt(x * 8, y * 8, 0, 0, 8, 8, 8)


    map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    me = me.Me()
    item = Item()

App()
