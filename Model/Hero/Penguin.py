from Model.Hero.Hero import *
class Penguin(Hero):
    def __init__(self, scale, x, y):
        super().__init__(scale, x, y)

    def figura(self):
        cuerpo= [1.5, 1, 6.5, 1, 6.5, 7.5 , 1.5, 7.5 ]
        pecho= [3, 1, 5, 1, 5, 5.5, 3, 5.5]
        piernas = [2, 0, 3, 0, 3, 1, 2, 1, #pierna izquierda
                   5, 0, 6, 0, 6, 1, 5, 1] # pierna derecha
        alas = [0, 3, 1.5, 3, 1.5, 6, #ala izquierda
                8, 3, 6.5, 3, 6.5, 6] #ala derecha
        ojos = [3.5, 5.5, 2, 5.5, 2, 6.8, #ojo izquierdo
                4.5, 5.5, 6, 5.5, 6, 6.8] #ojo derecho
        nariz= [4, 4, 4.5, 5, 3.5, 5]
        c = list(map(lambda x: self.scale * x, cuerpo))
        p = list(map(lambda  x: self.scale *x, pecho))
        pr= list(map(lambda  x: self.scale *x, piernas))
        a = list(map(lambda x: self.scale *x, alas))
        oj = list(map(lambda x: self.scale *x, ojos))
        n= list(map(lambda x: self.scale *x, nariz))

        #cuerpo y pecho
        glBegin(GL_QUADS)
        glColor3f(35 / 255, 35 / 255, 35 / 255)
        glVertex2f(c[0], c[1])
        glVertex2f(c[2], c[3])
        glVertex2f(c[4], c[5])
        glVertex2f(c[6], c[7])

        glVertex2f(pr[0], pr[1])
        glVertex2f(pr[2], pr[3])
        glVertex2f(pr[4], pr[5])
        glVertex2f(pr[6], pr[7])

        glVertex2f(pr[8], pr[9])
        glVertex2f(pr[10], pr[11])
        glVertex2f(pr[12], pr[13])
        glVertex2f(pr[14], pr[15])

        #pecho
        glColor3f(1, 1, 1)
        glVertex2f(p[0], p[1])
        glVertex2f(p[2], p[3])
        glVertex2f(p[4], p[5])
        glVertex2f(p[6], p[7])
        glEnd()

        #alas
        glBegin(GL_TRIANGLES)
        glColor3f(1, 1, 1)
        glVertex2f(a[0], a[1])
        glVertex2f(a[2], a[3])
        glVertex2f(a[4], a[5])

        glVertex2f(a[6], a[7])
        glVertex2f(a[8], a[9])
        glVertex2f(a[10], a[11])

        # ojos
        # ojo izquierdo
        glColor3f(0, 0, 0)
        glVertex2f(oj[0], oj[1])
        glVertex2f(oj[2], oj[3])
        glVertex2f(oj[4], oj[5])

        #ojo derecho
        glVertex2f(oj[6], oj[7])
        glVertex2f(oj[8], oj[9])
        glVertex2f(oj[10], oj[11])

        #nariz

        glColor3f(1, 69 / 255 , 0)
        glVertex2f(n[0], n[1])
        glVertex2f(n[2], n[3])
        glVertex2f(n[4], n[5])
        glEnd()

        #line loops
        glBegin(GL_LINE_LOOP)
        glColor3f(0, 0, 0)
        glVertex2f(c[0], c[1])
        glVertex2f(c[2], c[3])
        glVertex2f(c[4], c[5])
        glVertex2f(c[6], c[7])
        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(0, 0, 0)
        glVertex2f(pr[0], pr[1])
        glVertex2f(pr[2], pr[3])
        glVertex2f(pr[4], pr[5])
        glVertex2f(pr[6], pr[7])
        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(0, 0, 0)
        glVertex2f(pr[8], pr[9])
        glVertex2f(pr[10], pr[11])
        glVertex2f(pr[12], pr[13])
        glVertex2f(pr[14], pr[15])
        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(0, 0, 0)
        glVertex2f(a[0], a[1])
        glVertex2f(a[2], a[3])
        glVertex2f(a[4], a[5])
        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(0, 0, 0)
        glVertex2f(a[6], a[7])
        glVertex2f(a[8], a[9])
        glVertex2f(a[10], a[11])

        glEnd()