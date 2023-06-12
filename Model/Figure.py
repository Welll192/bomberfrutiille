from OpenGL.GL import *
from math import *
import random
import pygame


class Figure():

    def __init__(self,scale,x0,y0,rgb=(1.0, 1.0, 1.0)):
        '''

        :param scale:
        :param color:
        :param x0:
        :param y0:
        '''
        self.altura=8
        self.x0=x0
        self.y0=y0
        self.color=rgb
        self.scale=scale
        self.lista = 0
        self.step = self.scale * self.altura
        self.crear()

    #Cuando se utiliza GL_COMPILE como argumento de glNewList, se indica que los comandos OpenGL
    #que se ejecutan después deben compilarse y almacenarse en la lista de visualización.Esto significa
    #que los comandos no se ejecutan inmediatamente, sino que se almacenan en memoria para
    #su uso posterior.
    #Esto significa que los comandos no se ejecutan inmediatamente, sino que se almacenan en memoria
    # para su uso posterior.

    #Se encarga de crear la lista de visualización de la figura utilizando las funciones de OpenGL.
    def crear(self):
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)
        self.figura()
        glEndList()

    def dibujar(self):
        glPushMatrix()
        glColor3fv(self.color)
        glTranslatef(self.x0, self.y0, 0.0)
        glCallList(self.lista)
        glPopMatrix()

    def figura(self):
        pass

    def getPosition(self):
        return((self.x0, self.y0))


    def isDestroyed(self, x, y):
        if x== self.x0 and y== self.y0:
            return True
        else:
            return False


