from pygame.locals import *
from OpenGL.GLU import *
from Model.Model import *
from Model.PowerUps.Explosion import *

class View:
    def __init__(self,alto,ancho):
        '''

        :param alto: alto de la ventana del juego
        :param ancho: ancho de la ventana del juego

        '''
        self.alto=alto
        self.ancho=ancho
        self.pjs = []
        self.surface = None

    def update(self):
        self.model.removeHero()
        self.dibujar()

    def dibujar(self):
        # limpia la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for p in self.pjs:
            p.dibujar()

    def init(self):

        # init pygame
        pygame.init()
        self.surface = pygame.display.set_mode((self.ancho, self.alto), OPENGL | DOUBLEBUF)
        #pygame.display.set_caption(titulo)

        # init opengl

        glViewport(0, 0, self.ancho, self.alto)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0.0, self.ancho, 0.0, self.alto)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # definir variables de opengl
        glClearColor(0.0, 50/255, 0.0, 0.0)  # color del fondo
        glShadeModel(GL_SMOOTH)
        glClearDepth(1.0)
        # glDisable(GL_DEPTH_TEST)

        #init view objects
        self.model = Laberinto(5, 520, 600)
        self.pjs.append(self.model)
        return
