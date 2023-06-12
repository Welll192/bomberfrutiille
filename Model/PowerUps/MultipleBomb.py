from Model.PowerUps.Bomb import *


class MultipleBomb:
    def __init__(self, scale, x, y):
        self.altura=8
        self.scale = scale
        self.x0 = x - self.altura * self.scale / 2
        self.y0 = y -self.altura * self.scale / 2
        self.bombArray = []
        self.init()
        self.type = "multiplebomb"


    def init(self):
        Bomb1 = Bomb(2.5, 10+ self.x0, 10 + self.y0, 0)
        Bomb2 = Bomb(2.5, 20+ self.x0,  30+ self.y0, 0)
        Bomb3 = Bomb(2.5, 30+ self.x0, 10 + self.y0, 0)
        self.bombArray.append(Bomb1)
        self.bombArray.append(Bomb2)
        self.bombArray.append(Bomb3)

    def dibujar(self):
        for x in self.bombArray:
           x.dibujar()


    def figura(self):
        for x in self.bombArray:
           x.figura()

    def getPosition(self):
        x= self.x0 + self.altura * self.scale / 2
        y = self.y0 + self.altura * self.scale / 2
        return (x, y)
