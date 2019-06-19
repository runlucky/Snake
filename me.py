import pyxel

class Me:

    x = 0
    y = 0

    vx = 1
    vy = 0

    old_x = []
    old_y = []

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

        self.old_x = [self.x] + self.old_x
        self.old_y = [self.y] + self.old_y

        del self.old_x[20:]
        del self.old_y[20:]

        self.x += self.vx
        self.y += self.vy

        self.limit()

    def draw(self):
        for n in range(self.ghosts):
            pyxel.blt(self.old_x[n] * 8, self.old_y[n] * 8, 0, 0, 8, 8, 8)

        pyxel.blt(self.x * 8, self.y * 8, 0, 0, 0, 8, 8)

    def limit(self):
        self.x = max(self.x , 0)
        self.y = max(self.y , 0)
        self.x = min(self.x , 15)
        self.y = min(self.y, 15)

    ghosts = 0