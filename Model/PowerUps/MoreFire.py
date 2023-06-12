from Model.Figure import *

class MoreFire(Figure):
    def __init__(self, scale, x, y):
        super().__init__(scale, x, y)
        self.type = "morefire"

    def figura(self):
        fuego_exterior = [-1, -4, 1, -4, 1, 4, -1, 4, #fuego vertical
                          -4, -1, -4 ,1 , 4 , 1, 4 ,-1] # fuego horizontal
        f1 = list(map(lambda x: self.scale * x, fuego_exterior))
        fuego_interior = [-0.5, -4, 0.5, -4, 0.5, 4, -0.5, 4, # fuego vertical
                          -4, -0.5, -4, 0.5, 4 , 0.5, 4, -0.5] # fuego horizontal

        f2 = list(map(lambda x: self.scale * x, fuego_interior))
        
        glBegin(GL_QUADS)

        #fuego exterior
        glColor3f(1, 0, 0)
        glVertex2f(f1[0], f1[1])
        glVertex2f(f1[2], f1[3])
        glVertex2f(f1[4], f1[5])
        glVertex2f(f1[6], f1[7])

        glVertex2f(f1[8], f1[9])
        glVertex2f(f1[10], f1[11])
        glVertex2f(f1[12], f1[13])
        glVertex2f(f1[14], f1[15])
        
        #fuego interior

        glColor3f(1, 128 / 255, 0)
        glVertex2f(f2[0], f2[1])
        glVertex2f(f2[2], f2[3])
        glVertex2f(f2[4], f2[5])
        glVertex2f(f2[6], f2[7])

        glVertex2f(f2[8], f2[9])
        glVertex2f(f2[10], f2[11])
        glVertex2f(f2[12], f2[13])
        glVertex2f(f2[14], f2[15])
        
        glEnd()




