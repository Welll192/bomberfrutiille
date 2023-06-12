from Model.Figure import *
class MuroDestructible(Figure):
    def __init__(self, scale, x, y):
        super().__init__(scale, x, y)

    def random_gray(self):
        return (128 + random.randrange(-30,30,1) )/255
    def figura(self):
        ladrillo1= [-4,4, 4,4, 4,2 ,-4,2]
        ladrillo2= [-4,2,-4,-1, 1,-1, 1,2]
        ladrillo3= [1,2, 4,2, 4, -1, 1, -1]
        ladrillo4= [-4,-1, -1, -1, -1,-4, -4,-4]
        ladrillo5= [-1,-4, 4, -4,4 ,-1 , -1,-1]

        l = list(map(lambda x: self.scale * x, ladrillo1))
        l2 = list(map(lambda x: self.scale * x, ladrillo2))
        l3 = list(map(lambda x: self.scale * x, ladrillo3))
        l4 = list(map(lambda x: self.scale * x, ladrillo4))
        l5 = list(map(lambda x: self.scale * x, ladrillo5))


        #ladrillo 1
        glBegin(GL_QUADS)
        g1=self.random_gray()
        glColor3f(g1, g1, g1)
        glVertex2f(l[0], l[1])
        glVertex2f(l[2], l[3])
        glVertex2f(l[4], l[5])
        glVertex2f(l[6], l[7])
        
        #ladrillo2
        g2 = self.random_gray()
        glColor3f(g2, g2, g2)
        glVertex2f(l2[0], l2[1])
        glVertex2f(l2[2], l2[3])
        glVertex2f(l2[4], l2[5])
        glVertex2f(l2[6], l2[7])
        
        #ladrillo3
        g3 = self.random_gray()
        glColor3f(g3, g3, g3)
        glVertex2f(l3[0], l3[1])
        glVertex2f(l3[2], l3[3])
        glVertex2f(l3[4], l3[5])
        glVertex2f(l3[6], l3[7])
        
        #ladrillo4
        g4=self.random_gray()
        glColor3f(g4, g4, g4)
        glVertex2f(l4[0], l4[1])
        glVertex2f(l4[2], l4[3])
        glVertex2f(l4[4], l4[5])
        glVertex2f(l4[6], l4[7])
        
        #ladrillo5
        g5 = self.random_gray()
        glColor3f(g5, g5, g5)
        glColor3f(128 / 255, 128 / 255, 128 / 255)
        glVertex2f(l5[0], l5[1])
        glVertex2f(l5[2], l5[3])
        glVertex2f(l5[4], l5[5])
        glVertex2f(l5[6], l5[7])
        glEnd()

        #borderados
        glBegin(GL_LINE_LOOP)
        glColor3f(20 / 255, 20 / 255, 20 / 255)
        glVertex2f(l[0], l[1])
        glVertex2f(l[2], l[3])
        glVertex2f(l[4], l[5])
        glVertex2f(l[6], l[7])

        glVertex2f(l2[0], l2[1])
        glVertex2f(l2[2], l2[3])
        glVertex2f(l2[4], l2[5])
        glVertex2f(l2[6], l2[7])

        glVertex2f(l3[0], l3[1])
        glVertex2f(l3[2], l3[3])
        glVertex2f(l3[4], l3[5])
        glVertex2f(l3[6], l3[7])

        glVertex2f(l4[0], l4[1])
        glVertex2f(l4[2], l4[3])
        glVertex2f(l4[4], l4[5])
        glVertex2f(l4[6], l4[7])
        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(20 / 255, 20 / 255, 20 / 255)

        glVertex2f(l5[0], l5[1])
        glVertex2f(l5[2], l5[3])
        glVertex2f(l5[4], l5[5])
        glVertex2f(l5[6], l5[7])

        glEnd()