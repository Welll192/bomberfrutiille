from Model.Enemy.Enemy import *

class Melon(Enemy):

    def __init__(self, scale, x, y):
        super().__init__(scale,x,y) ## inicializa los atributos heredados de la clase padre
        ##Se iniciliza la posición desplazando hacia la izq y arriba para centrar la figura
        self.x0 -= self.altura * self.scale / 2
        self.y0 -= self.altura * self.scale / 2

    def figura(self):
        #Brazos
        brazos= [0, 4, 1, 4, 1, 5, 0 ,5, # brazo izquierdo
                8, 4, 7, 4, 7, 5 ,8 ,5]  #brazo derecho
        #Piernas
        piernas=[3, 0, 2, 0, 2, 3 ,3, 3, # pierna izquierda
                 5, 0, 6, 0, 6, 3, 5, 3]#pierna derecha
        #torzo
        torzo = [4,7, 4,6]
        #ojos
        ojos = [3,5, 5, 5]

        p = list(map(lambda x: self.scale * x, piernas))
        b = list(map(lambda x: self.scale * x, brazos))
        t = list(map(lambda x: self.scale * x, torzo))
        o = list(map(lambda x: self.scale * x, ojos))

        #brazos
        glBegin(GL_QUADS) #dibuja cuadrilatero
        glColor3f(0, 0, 0) # negro

        # brazo izquierdo
        glVertex2f(b[0], b[1])
        glVertex2f(b[2], b[3])
        glVertex2f(b[4], b[5])
        glVertex2f(b[6], b[7])

        # brazo derecho
        glVertex2f(b[8], b[9])
        glVertex2f(b[10], b[11])
        glVertex2f(b[12], b[13])
        glVertex2f(b[14], b[15])

        # piernas
        # pierna izquierda

        glColor3f(0, 0, 0)
        glVertex2f(p[0], p[1])
        glVertex2f(p[2], p[3])
        glVertex2f(p[4], p[5])
        glVertex2f(p[6], p[7])

        # pierna derecha

        glVertex2f(p[8], p[9])
        glVertex2f(p[10], p[11])
        glVertex2f(p[12], p[13])
        glVertex2f(p[14], p[15])
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0.5, 0) ##verde oscuro
        glVertex2f(t[0], t[1])
        radio = 4.5 * self.scale
        ang = 2 * pi / 20

        for i in range(10,21):
            ang_i = ang * i
            glVertex(t[0] + cos(ang_i) * radio, t[1] + sin(ang_i) * radio)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 0.5, 0)
        glVertex2f(t[2], t[3])
        radio = 3 * self.scale
        ang = 2 * pi / 20
        for i in range(10, 21):
            ang_i = ang * i
            glVertex(t[2] + cos(ang_i) * radio, t[3] + sin(ang_i) * radio)

        glEnd()

        #ojos
        #ojo izquierdo
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0.1, 0)
        glVertex2f(o[0], o[1])
        radio = 0.5 * self.scale
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(o[0] + cos(ang_i) * radio, o[1] + sin(ang_i) * radio)
        glEnd()

        #ojo derecho
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0.1, 0)
        glVertex2f(o[2], o[3])
        radio = 0.5 * self.scale
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(o[2] + cos(ang_i) * radio, o[3] + sin(ang_i) * radio)
        glEnd()

    def getPosition(self):
        xpos = self.x0 + self.altura * self.scale / 2
        ypos = self.y0 + self.altura * self.scale / 2
        return (xpos, ypos)
