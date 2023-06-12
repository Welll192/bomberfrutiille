from Model.Hero.Hero import *
class Frutilla(Hero):
    def __init__(self, scale, x, y):
        super().__init__(scale,x,y)

    def figura(self):

        cuerpo=[0,-3,4,3,-4,3, #cuerpo
                0, -2, -2, 4, 2, 4, #tallo
                4,0,4,1,1,1,1,0, #brazo d
                -4, 0, -4, 1,-1,1,-1 ,0, #brazo i
                ]
        pies=[2,0, 1,0, 1, -3, 2, -3,#pie der
              -2,0, -1,0,-1, -3, -2, -3] #pie izq

        ojos=[ 3, 2, -3 ,2]
        l = list(map(lambda x: self.scale * x, cuerpo))
        p= list(map(lambda x: self.scale * x, pies))
        o= list(map(lambda x: (int(sqrt(self.scale))) * x, ojos))


        #brazos

        #brazo derecho
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glVertex2f(l[12], l[13])
        glVertex2f(l[14], l[15])
        glVertex2f(l[16], l[17])
        glVertex2f(l[18], l[19])
        glEnd()


        #brazo izquierdo

        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glVertex2f(l[20], l[21])
        glVertex2f(l[22], l[23])
        glVertex2f(l[24], l[25])
        glVertex2f(l[26], l[27])
        glEnd()

        #pierna
        # pierna derecha

        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glVertex2f(p[0], p[1])
        glVertex2f(p[2], p[3])
        glVertex2f(p[4], p[5])
        glVertex2f(p[6], p[7])
        glEnd()

        # pierna izquierda

        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glVertex2f(p[8], p[9])
        glVertex2f(p[10], p[11])
        glVertex2f(p[12], p[13])
        glVertex2f(p[14], p[15])
        glEnd()

        # torzo

        glBegin(GL_TRIANGLES)
        glColor3f(0, 230 / 255, 0)
        glVertex2f(l[6], l[7])
        glVertex2f(l[8], l[9])
        glVertex2f(l[10], l[11])
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(255 / 255, 0, 66 / 255)
        glVertex2f(l[0], l[1])
        glVertex2f(l[2], l[3])
        glVertex2f(l[4], l[5])
        glEnd()

        #line loop
        glBegin(GL_LINE_LOOP)
        glColor3f(148/255, 0, 118/255)
        glVertex2f(l[0], l[1])
        glVertex2f(l[2], l[3])
        glVertex2f(l[4], l[5])
        glEnd()

        #ojos
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0.1, 0)
        glVertex2f(o[0], o[1])
        radio = 1* int(sqrt(self.scale))
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(o[0] + cos(ang_i) * radio, o[1] + sin(ang_i) * radio)

        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0.1, 0)
        glVertex2f(o[2], o[3])
        radio = 1* int(sqrt(self.scale))
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(o[2] + cos(ang_i) * radio, o[3] + sin(ang_i) * radio)

        glEnd()