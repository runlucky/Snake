import pyxel


class Score:
    point = 0

    def draw(self):
        pyxel.text(1, 1, str(self.point), 6)