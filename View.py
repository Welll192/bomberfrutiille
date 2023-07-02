from OpenGL.GLU import *
from pygame.locals import *

from Model.Model import *
from Model.PowerUps.Explosion import *
from PIL import Image


class View:
    def __init__(self, alto, ancho):
        '''
        alto: alto de la ventana del juego
        ancho: ancho de la ventana del juego
        '''
        self.alto = alto
        self.ancho = ancho
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
        # pygame.display.set_caption(titulo)

        # init opengl
        glViewport(0, 0, self.ancho, self.alto)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0.0, self.ancho, 0.0, self.alto)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # definir variables de opengl
        glClearColor(0.0, 50 / 255, 0.0, 0.0)  # color del fondo
        glShadeModel(GL_SMOOTH)
        glClearDepth(1.0)

        self.model = Laberinto(5, 520, 600)
        self.pjs.append(self.model)
        return

    def viewFinal(self):
        if self.gano or self.perdio:
            self.showImage()

    def draw_image(self, image_data, width, height):
        glRasterPos2f(40, 0)
        glDrawPixels(width, height, GL_RGB, GL_UNSIGNED_BYTE, image_data)

    def showImage(self):
        global image_path, nombre_archivo
        self.model.laberinto = []  # discretizacio del laberinto
        self.model.ocupados = []
        self.model.muros_indest = []
        self.model.muros_dest = []
        self.model.enemies = []
        self.model.powerups = []
        self.model.explosion = []

        glClearColor(0, 0, 0, 0)  # Cambia el color del fondo a negro

        # Obtén la ruta del directorio actual
        directorio_actual = os.getcwd()

        # Nombre de la carpeta en la que se encuentra el archivo
        nombre_carpeta = "Image"

        if (self.gano):
            nombre_archivo = "winner.jpg"
        elif (self.perdio):
            image_path = "loser.jpg"

        image_path = os.path.join(directorio_actual, nombre_carpeta,
                                  nombre_archivo)  # Reemplaza con la ruta de tu imagen
        image = Image.open(image_path)
        image_data = image.tobytes()
        width, height = image.size

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw_image(image_data, width, height)
