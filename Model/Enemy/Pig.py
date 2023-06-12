from Model.Enemy.Enemy import *

class Pig(Enemy):
    def __init__(self, scale, x, y):
        super().__init__(scale, x, y)
        self.x0 -= self.altura * self.scale / 2
        self.y0 -= self.altura * self.scale / 2

    def figura(self):
        cuerpo=[4,4,4]
        orejas=[0, 6, 2, 8, 3, 6, #oreja izquierda
                5, 6, 6, 8, 8, 6] #oreja derecha
        ojos= [2.5, 4.5, #ojo izquierdo
               5.5, 4.5] #ojo derecho
        nariz=[3, 2, 3, 3.5, 5, 2, 5, 3.5]
        c = list(map(lambda x: self.scale * x, cuerpo))
        o = list(map(lambda x: self.scale * x, orejas))
        oj = list(map(lambda x: self.scale * x, ojos))
        n = list(map(lambda x: self.scale * x, nariz))

        #cuerpo
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(255 / 255, 182 / 255 , 193 / 255)
        glVertex2f(c[0], c[1])
        radio = c[2]
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(c[0] + cos(ang_i) * radio, c[1] + sin(ang_i) * radio)

        glEnd()

        #orejas
        glBegin(GL_TRIANGLES)
        glColor3f(255 / 255, 105 / 255, 180 / 255)
        glVertex2f(o[0], o[1])
        glVertex2f(o[2], o[3])
        glVertex2f(o[4], o[5])

        glVertex2f(o[6], o[7])
        glVertex2f(o[8], o[9])
        glVertex2f(o[10], o[11])
        glEnd()

        # line loop
        glBegin(GL_LINE_LOOP)
        glColor3f(148 / 255, 0, 118 / 255)
        glVertex2f(o[0], o[1])
        glVertex2f(o[2], o[3])
        glVertex2f(o[4], o[5])
        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(148 / 255, 0, 118 / 255)
        glVertex2f(o[6], o[7])
        glVertex2f(o[8], o[9])
        glVertex2f(o[10], o[11])
        glEnd()

        #nariz
        glBegin(GL_QUADS)
        glColor3f(255 /255, 20 / 255, 147 / 255)
        glVertex2f(n[0], n[1])
        glVertex2f(n[2], n[3])
        glVertex2f(n[4], n[5])
        glVertex2f(n[6], n[7])
        glEnd()

        # ojos
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)
        glVertex2f(oj[0], oj[1])
        radio = 0.5 * self.scale
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(oj[0] + cos(ang_i) * radio, oj[1] + sin(ang_i) * radio)

        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)
        glVertex2f(oj[2], oj[3])
        radio = 0.5 * self.scale
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(oj[2] + cos(ang_i) * radio, oj[3] + sin(ang_i) * radio)

        glEnd()

    def getPosition(self):
        xpos = self.x0 + self.altura * self.scale / 2
        ypos = self.y0 + self.altura * self.scale / 2
        return (xpos, ypos)