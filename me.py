import pyxel

class Me:

    x = 0
    y = 0

    vx = 1
    vy = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.vx = -1
            self.vy = 0
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.vx = 1
            self.vy = 0
        elif pyxel.btnp(pyxel.KEY_UP):
            self.vx = 0
            self.vy = -1
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.vx = 0
            self.vy = 1

        self.x += self.vx
        self.y += self.vy

        self.limit()

    def draw(self):
        pyxel.blt(self.x * 8, self.y * 8, 0, 0, 0, 8, 8)

    def limit(self):
        self.x = max(self.x , 0)
        self.y = max(self.y , 0)
        self.x = min(self.x , 15)
        self.y = min(self.y , 15)