from Model.Enemy.Enemy import *

class Robot(Enemy):
    def __init__(self, scale, x, y):
        super().__init__(scale,x,y)

    def figura(self):
        cabeza=[-3,4 ,3 ,4, 3, 1, -3, 1]
        c = list(map(lambda x: self.scale * x, cabeza))
        oreja1=[-3,3, -4, 3, -4, 2, -3, 2]
        oreja2=[3,3, 4,3 ,4,2 ,3,2]
        o1=list(map(lambda x: self.scale * x, oreja1))
        o2 = list(map(lambda x: self.scale * x, oreja2))
        ojos1=[-2,3, -2,2, 2,2 ,2,3]
        oj1 = list(map(lambda x: self.scale * x, ojos1))
        cuerpo = [-3, 1, 3, 1, 3, -1, -3, -1,# torzo superior
                  -2,-1, 2, -1, 2, -3 ,-2, -3,# torzo medio
                  1, -3, 1, -4, -1, -4, -1, -3 ]# torzo inferior
        cu = list(map(lambda x: self.scale * x, cuerpo))

        brazos=[-3, 1, -4, 1, -4, -2, -3, -2, #brazo izquierd
                3,1, 4,1, 4 ,-2 ,3, -2] #brazo derecho
        b = list(map(lambda x: self.scale * x, brazos))

        #cabeza
        glBegin(GL_QUADS)
        glColor3f(192/255, 192 /255 ,192/255)
        glVertex2f(c[0], c[1])
        glVertex2f(c[2], c[3])
        glVertex2f(c[4], c[5])
        glVertex2f(c[6], c[7])

        #oreja izquierda
        glVertex2f(o1[0], o1[1])
        glVertex2f(o1[2], o1[3])
        glVertex2f(o1[4], o1[5])
        glVertex2f(o1[6], o1[7])

        # oreja derecha
        glVertex2f(o2[0], o2[1])
        glVertex2f(o2[2], o2[3])
        glVertex2f(o2[4], o2[5])
        glVertex2f(o2[6], o2[7])

        #lentes
        glColor3f(1, 140/255, 0)
        glVertex2f(oj1[0], oj1[1])
        glVertex2f(oj1[2], oj1[3])
        glVertex2f(oj1[4], oj1[5])
        glVertex2f(oj1[6], oj1[7])

        #cuerpo

        glColor3f(192 / 255, 192 / 255, 192 / 255)
        glVertex2f(cu[8], cu[9])
        glVertex2f(cu[10], cu[11])
        glVertex2f(cu[12], cu[13])
        glVertex2f(cu[14], cu[15])

        glColor3f(47 / 255, 79 / 255, 79 / 255)
        glVertex2f(cu[0], cu[1])
        glVertex2f(cu[2], cu[3])
        glVertex2f(cu[4], cu[5])
        glVertex2f(cu[6], cu[7])



        glColor3f(0, 0, 0)
        glVertex2f(cu[16], cu[17])
        glVertex2f(cu[18], cu[19])
        glVertex2f(cu[20], cu[21])
        glVertex2f(cu[22], cu[23])

        #brazo izquierdo
        glColor3f(0, 0, 0)
        glVertex2f(b[0], b[1])
        glVertex2f(b[2], b[3])
        glVertex2f(b[4], b[5])
        glVertex2f(b[6], b[7])
        #brazo derecho
        glVertex2f(b[8], b[9])
        glVertex2f(b[10], b[11])
        glVertex2f(b[12], b[13])
        glVertex2f(b[14], b[15])
        glEnd()

