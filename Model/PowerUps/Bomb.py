from Model.Figure import *

class Bomb(Figure):
    def __init__(self, scale, x, y, time):
        super().__init__(scale, x, y)
        self.x0-= self.altura*self.scale/2
        self.y0 -= self.altura * self.scale / 2
        self.timetolive= time+3


    def figura(self):
        cuerpo= [4,4,3, 4, 4, 2.5]
        sombreado= [6, 6, 1.2]
        llama= [7.5, 7, 7, 7.5, 5.5, 6, 6, 5.5]
        c = list(map(lambda x: self.scale * x, cuerpo))
        s =  list(map(lambda x: self.scale * x, sombreado))
        l= list(map(lambda x: self.scale * x, llama))


        # cuerpo
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)
        glVertex2f(c[0], c[1])
        radio = c[2]
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(c[0] + cos(ang_i) * radio, c[1] + sin(ang_i) * radio)

        #sombreado
        glColor3f(0.1, 0.1, 0.2)
        glVertex2f(c[3], c[4])
        radio = c[5]
        ang = 2 * pi / 20
        for i in range(6, 20):
            ang_i = ang * i
            glVertex(c[3] + cos(ang_i) * radio, c[4] + sin(ang_i) * radio)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.1, 0.1, 0.3)
        glVertex2f(s[0], s[1])
        radio = s[2]
        ang = 2 * pi / 20
        for i in range(8, 18):
            ang_i = ang * i
            glVertex(s[0] + cos(ang_i) * radio, s[1] + sin(ang_i) * radio)
        glEnd()

        #llama
        glBegin(GL_QUADS)
        glColor3f(1, 69 / 255 , 0)
        glVertex2f(l[0], l[1])
        glVertex2f(l[2], l[3])
        glVertex2f(l[4], l[5])
        glVertex2f(l[6], l[7])
        glEnd()

    def isReady(self, time):
        return time >= self.timetolive

    def destroyItems(self, laberinto):
        laberinto.removeItems(self)

    def destroyMoreItems(self, laberinto):
        laberinto.removeMoreItems(self)

    def getPosition(self):
        xpos = self.x0  + self.altura * self.scale / 2
        ypos = self.y0 + self.altura * self.scale / 2
        return (xpos, ypos)

    def getTime(self):
        return self.timetolive

