from Model.Figure import *
class Muro(Figure):
    def __init__(self, scale, x, y):
        super().__init__(scale, x, y)

    def figura(self):
        muro = [-4, -4,
                -4, 4,
                4, 4,
                4, -4]
        muro2 = [-3, -4,
                 -4, -4,
                 -4, 4,
                 -3, 4,
                 4, -4,
                 4, -3,
                 -4,-3,
                 -4, -4

                 ]

        muro3 = [-3, 4,
                 4, 4,
                 4, 3,
                 -3, 3,
                 4, -3,
                 3, -3,
                 3, 4,
                 4, 4]
        lineas = [-4, -4,
                  -4, 4,
                  4, 4,
                  4, -4]

        m = list(map(lambda x: self.scale * x, muro))
        m2 = list(map(lambda x: self.scale * x, muro2))
        m3 = list(map(lambda x: self.scale * x, muro3))
        linea = list(map(lambda x: self.scale * x, lineas))

        #cuadrado pricipal
        glBegin(GL_QUADS)
        glColor3f(128 / 255, 128 / 255, 128 / 255)
        glVertex2f(m[0], m[1])
        glVertex2f(m[2], m[3])
        glVertex2f(m[4], m[5])
        glVertex2f(m[6], m[7])
        glEnd()

        #sombreado
        glBegin(GL_QUADS)
        glColor3f(90 / 255, 90 / 255, 90 / 255)
        glVertex2f(m2[0], m2[1])
        glVertex2f(m2[2], m2[3])
        glVertex2f(m2[4], m2[5])
        glVertex2f(m2[6], m2[7])

        glVertex2f(m2[8], m2[9])
        glVertex2f(m2[10], m2[11])
        glVertex2f(m2[12], m2[13])
        glVertex2f(m2[14], m2[15])

        glEnd()
        #iluminación
        glBegin(GL_QUADS)
        glColor3f(160 / 255, 160 / 255, 160 / 255)
        glVertex2f(m3[0], m3[1])
        glVertex2f(m3[2], m3[3])
        glVertex2f(m3[4], m3[5])
        glVertex2f(m3[6], m3[7])
        glVertex2f(m3[8], m3[9])
        glVertex2f(m3[10], m3[11])
        glVertex2f(m3[12], m3[13])
        glVertex2f(m3[14], m3[15])
        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(20 / 255, 20 / 255, 20 / 255)
        glVertex2f(linea[0], linea[1])
        glVertex2f(linea[2], linea[3])
        glVertex2f(linea[4], linea[5])
        glVertex2f(linea[6], linea[7])
        glEnd()



