from Model.Figure import *
class Explosion(Figure):
    def __init__(self, scale, x, y, time):
        super().__init__(scale, x, y)
        self.x0-= self.altura*self.scale/2
        self.y0 -= self.altura * self.scale / 2
        self.timetolive= time+2

    def figura(self):
        t1=[2,4, 6,4, 4, 8 ]
        t2=[3.5,4, 4.5, 4, 4, 6]
        c1=[4,4, 2]
        c2= [4,4, 1]
        T1 = list(map(lambda x: self.scale * x, t1))
        T2 = list(map(lambda x: self.scale * x, t2))
        C1 = list(map(lambda x: self.scale * x, c1))
        C2 = list(map(lambda x: self.scale * x, c2))
        # t1
        glBegin(GL_TRIANGLES)
        glColor3f(1, 69 / 255 , 0)
        glVertex2f(T1[0], T1[1])
        glVertex2f(T1[2], T1[3])
        glVertex2f(T1[4], T1[5])
        glEnd()

        # c1
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 69 / 255 , 0)
        glVertex2f(C1[0], C1[1])
        radio = C1[2]
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(C1[0] + cos(ang_i) * radio, C1[1] + sin(ang_i) * radio)
        glEnd()

        # t2
        glBegin(GL_TRIANGLES)
        glColor3f(1, 1, 0)
        glVertex2f(T2[0], T2[1])
        glVertex2f(T2[2], T1[3])
        glVertex2f(T2[4], T2[5])
        glEnd()

        # c2
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 1, 0)
        glVertex2f(C2[0], C2[1])
        radio = C2[2]
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(C2[0] + cos(ang_i) * radio, C2[1] + sin(ang_i) * radio)
        glEnd()

    def getPosition(self):
        xpos = self.x0 + self.altura * self.scale / 2
        ypos = self.y0 + self.altura * self.scale / 2
        return (xpos, ypos)

    def isReady(self, time):
        return time >= self.timetolive

    def burn(self,time, laberinto):
        if self.isReady(time):
            laberinto.removeExplosion(self)
            return
        else:
            laberinto.burnItems(self)
