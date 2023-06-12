from Model.Figure import *

class Enemy(Figure):
    def __init__(self, scale, x, y):
        super().__init__(scale,x,y)
        self.velocity= 300 # 300 milisegundos
        self.t0= 0 # tiempo inicial

    def move(self, laberinto, time):
        #laberinto: escenario
        #time: tiempo actual

        #Se verifica si ha pasado un tiempo mayor que "velocity" desde le último movimiento registrado
        if time-self.t0 > self.velocity:
            self.t0= time # Se define el tiempo inicial
            pos = self.getPosition() #Obtiene posición
            x = pos[0]
            y = pos[1]
            xstep= random.choice([-1, 0, 1]) #Elige movimiento aleatorio

            if xstep != 0:
                ystep = 0
            else:
                ystep = random.choice([-1, 0, 1])

            ##Verifica si la nueva posición está ocupada
            if (x + xstep * self.step, y + ystep * self.step) in laberinto.ocupados:
                return
            else:
                self.x0 += xstep * self.step
                self.y0 += ystep * self.step

    #verifica si la posición del enemigo es igual a la posición del héroe pasado
    def killHero(self,hero):
        return self.getPosition()==hero.getPosition()