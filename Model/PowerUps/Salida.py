from Model.Figure import *

class Salida(Figure):
    def __init__(self, scale, x, y):
        super().__init__(scale, x, y)
        self.type="salida"

    def figura(self):
        cuadrado = [-4, -4, -4, 4, 4, 4, 4, -4]
        c = list(map(lambda x: self.scale * x, cuadrado))

        glBegin(GL_QUADS)
        # cuadrado de fondo
        glColor3f(1, 1, 1)
        glVertex2f(c[0], c[1])
        glVertex2f(c[2], c[3])
        glVertex2f(c[4], c[5])
        glVertex2f(c[6], c[7])
        glEnd()