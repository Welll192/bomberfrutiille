from View import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla
'''cam = cv2.VideoCapture(0)

cam.set(3, 30) # largo
cam.set(2, 20) # alto
cam.set(10, 500) # brillo / luminosidad'''


class Controller:
    def __init__(self):
        self.V = View(520, 600)
        self.V.init()

    def update(self):
        run = True
        while run:
            time = int(pygame.time.get_ticks() / 1000)
            '''
            check, img = cam.read()
            cv2.imshow('Webcam', img)'''

            self.V.model.hero.removeBomb(self.V.model, time)
            self.V.model.checkExplosion(time)

            if self.V.model.hero.salida:
                run = False
                self.V.gano = True
                self.V.viewFinal()

            if self.V.model.hero.dead:
                run = False
                self.V.perdio = True
                self.V.viewFinal()

            for e in self.V.model.enemies:
                e.move(self.V.model, pygame.time.get_ticks())

            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False

                if event.type == KEYDOWN:

                    if event.key == K_SPACE:
                        pass

                    if event.key == K_RIGHT:
                        self.V.model.hero.move(self.V.model, 1, 0)

                    if event.key == K_LEFT:
                        self.V.model.hero.move(self.V.model, -1, 0)

                    if event.key == K_UP:
                        self.V.model.hero.move(self.V.model, 0, 1)

                    if event.key == K_DOWN:
                        self.V.model.hero.move(self.V.model, 0, -1)

                    if event.key == K_a:
                        self.V.model.hero.putBomb(self.V.model, time)

            pygame.display.flip()  # actualizar pantalla
            pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps
            self.V.update()

        pygame.time.wait(2000)
        pygame.quit()
