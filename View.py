from pygame.locals import *
from OpenGL.GLU import *
from Model.Model import *
from Model.PowerUps.Explosion import *
from freetype import *
from OpenGL.GLUT import *
from PIL import Image
import numpy as np

class View:
    def __init__(self,alto,ancho):
        '''
        alto: alto de la ventana del juego
        ancho: ancho de la ventana del juego
        '''
        self.alto=alto
        self.ancho=ancho
        self.pjs = []
        self.surface = None
        self.perdio = False
        self.gano = False

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
        

        self.model = Laberinto(5, 520, 600)
        self.pjs.append(self.model)
        return
    
    def viewFinal(self):
        if self.gano or self.perdio:
            self.showImage()
            
    def draw_image(self,image_data, width, height):
        glRasterPos2f(40,0)
        glDrawPixels(width, height, GL_RGB, GL_UNSIGNED_BYTE, image_data)

    def showImage(self):
        self.model.laberinto=[] #discretizacio del laberinto
        self.model.ocupados=[]
        self.model.muros_indest=[]
        self.model.muros_dest=[]
        self.model.enemies= []
        self.model.powerups=[]
        self.model.explosion= []
        
        glClearColor(0,0, 0, 0)  # Cambia el color del fondo a negro
        
        if(self.gano):
            image_path = "winner.jpg"  # Reemplaza con la ruta de tu imagen
        elif(self.perdio):
            image_path = "loser.jpg"

        image = Image.open(image_path)
        image_data = image.tobytes()
        width, height = image.size
       
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw_image(image_data,width, height)