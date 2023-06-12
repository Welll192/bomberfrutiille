from Model.Figure import *
from Model.PowerUps.Bomb import *

class Hero(Figure):
    def __init__(self, scale, x, y):
        super().__init__(scale,x,y)
        self.bombas = []
        self.maxBomb=2
        self.moreFire = False
        self.salida = False
        self.dead = False

    def move(self, laberinto, xstep, ystep):
        pos= self.getPosition()
        x=pos[0]
        y=pos[1]
        if (x + xstep*self.step, y + ystep*self.step) in laberinto.ocupados:
            return
        else:
            self.x0+= xstep*self.step
            self.y0+= ystep*self.step
            laberinto.givePowerup(self)

    def dibujar(self):
        super(Hero, self).dibujar()
        for b in self.bombas:
            b.dibujar()

    def getPowerup(self, power):
        if power.type == "multiplebomb":
            self.maxBomb= 5
        if power.type == "morefire":
            self.moreFire= True
        if power.type == "salida":
            self.salida = True


    def putBomb(self, laberinto, time):
        if self.bombas.__len__()>=self.maxBomb:
            return

        pos= self.getPosition()
        if pos in laberinto.ocupados:
            return
        else:
            self.bombas.append(Bomb(self.scale, self.x0, self.y0, time))
            laberinto.putBomb(pos, time)

    def removeBomb(self, laberinto, time):
        for b in self.bombas:
            if b.isReady(time):
                self.bombas.remove(b)
                if self.moreFire:
                    b.destroyMoreItems(laberinto)
                    return
                b.destroyItems(laberinto)

    def isKilled(self):
        self.dead= True
