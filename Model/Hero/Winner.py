from Model.Hero.Hero import *
class Winner(Figure):
    def __init__(self, scale, x, y):
        super().__init__(scale,x,y)

    def figura(self):
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.9, 0.9)
        glVertex2f(-0.8, 0.7)
        glVertex2f(-0.7, 0.9)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(-0.7, 0.9)
        glVertex2f(-0.6, 0.7)
        glVertex2f(-0.5, 0.9)
        glVertex2f(-0.4, 0.7)
        glEnd()

        glBegin(GL_TRIANGLES)
        glVertex2f(-0.4, 0.7)
        glVertex2f(-0.3, 0.9)
        glVertex2f(-0.2, 0.7)
        glEnd()

    
        glBegin(GL_QUADS)
        glVertex2f(-0.1, 0.9)
        glVertex2f(-0.1, 0.7)
        glVertex2f(0.1, 0.7)
        glVertex2f(0.1, 0.9)
        glEnd()

   
        glBegin(GL_TRIANGLES)
        glVertex2f(0.3, 0.9)
        glVertex2f(0.3, 0.7)
        glVertex2f(0.5, 0.9)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(0.5, 0.9)
        glVertex2f(0.7, 0.9)
        glVertex2f(0.7, 0.7)
        glVertex2f(0.5, 0.7)
        glEnd()

        glBegin(GL_TRIANGLES)
        glVertex2f(0.7, 0.7)
        glVertex2f(0.7, 0.9)
        glVertex2f(0.9, 0.7)
        glEnd()

    
        glBegin(GL_QUADS)
        glVertex2f(1.1, 0.9)
        glVertex2f(1.1, 0.7)
        glVertex2f(1.3, 0.7)
        glVertex2f(1.3, 0.9)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(1.1, 0.8)
        glVertex2f(1.2, 0.8)
        glVertex2f(1.2, 0.7)
        glVertex2f(1.1, 0.7)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(1.1, 0.9)
        glVertex2f(1.2, 0.9)
        glVertex2f(1.2, 0.8)
        glVertex2f(1.1, 0.8)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(1.1, 0.9)
        glVertex2f(1.3, 0.9)
        glVertex2f(1.3, 0.8)
        glVertex2f(1.1, 0.8)
        glEnd()

    
        glBegin(GL_QUADS)
        glVertex2f(1.5, 0.9)
        glVertex2f(1.5, 0.7)
        glVertex2f(1.7, 0.7)
        glVertex2f(1.7, 0.9)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(1.5, 0.9)
        glVertex2f(1.7, 0.9)
        glVertex2f(1.7, 0.8)
        glVertex2f(1.5, 0.8)
        glEnd()

        glBegin(GL_TRIANGLES)
        glVertex2f(1.7, 0.8)
        glVertex2f(1.7, 0.9)
        glVertex2f(1.9, 0.7)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(1.7, 0.8)
        glVertex2f(1.9, 0.7)
        glVertex2f(1.9, 0.7)
        glVertex2f(1.9, 0.8)
        glEnd()

        glBegin(GL_LINES)
        glVertex2f(1.7, 0.8)
        glVertex2f(1.9, 0.7)
        glEnd()

        # def dibujar():
        #     glClear(GL_COLOR_BUFFER_BIT)
        #     glColor3f(1.0, 1.0, 1.0)

        # Dibujar la palabra "WINNER"
        # dibujar_letra_W()
        # dibujar_letra_I()
        # dibujar_letra_N()
        # dibujar_letra_N()
        # dibujar_letra_E()
        # dibujar_letra_R()


      