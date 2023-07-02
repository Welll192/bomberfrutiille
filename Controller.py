import cv2
import mediapipe as mp
import numpy as np
from View import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


class Controller:
    def __init__(self):
        self.V = View(520, 600)
        self.V.init()
        self.video = cv2.VideoCapture(0)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mano = mp.solutions.hands

    # Función para detectar si un puño está cerrado
    def detectar_puno(self, mano):
        puntos = np.array([[p.x, p.y, p.z] for p in mano.landmark])
        dedo_pulgar = puntos[4] - puntos[2]
        dedo_indice = puntos[8] - puntos[6]
        dedo_medio = puntos[12] - puntos[10]
        dedo_anular = puntos[16] - puntos[14]
        dedo_menique = puntos[20] - puntos[18]

        if (dedo_pulgar[2] > 0 and dedo_indice[2] > 0 and dedo_medio[2] > 0 and dedo_anular[2] > 0 and dedo_menique[
            2] > 0):
            dedo_pulgar_angulo = np.arctan2(dedo_pulgar[1], dedo_pulgar[0])
            dedo_indice_angulo = np.arctan2(dedo_indice[1], dedo_indice[0])
            dedo_medio_angulo = np.arctan2(dedo_medio[1], dedo_medio[0])
            dedo_anular_angulo = np.arctan2(dedo_anular[1], dedo_anular[0])
            dedo_menique_angulo = np.arctan2(dedo_menique[1], dedo_menique[0])

            if dedo_pulgar_angulo > dedo_indice_angulo > dedo_medio_angulo > dedo_anular_angulo > dedo_menique_angulo:
                return True

        return False


    def update(self):
        run = True
        while run:
            time = int(pygame.time.get_ticks()/100)
            self.V.model.hero.removeBomb(self.V.model, time)
            self.V.model.checkExplosion(time)

            drawing_spec = self.mp_drawing.DrawingSpec(thickness=2, circle_radius=1)
            manos = self.mano.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
            ret, frame = self.video.read()

            if not ret:
                run = False #no se inicia la camara

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = manos.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if self.V.model.hero.salida:
                run = False
                self.V.gano = True
                self.V.viewFinal()

            if self.V.model.hero.dead:
                run = False
                self.V.perdio = True
                self.V.viewFinal()

            for enemy in self.V.model.enemies:
                enemy.move(self.V.model, pygame.time.get_ticks())

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mano.HAND_CONNECTIONS, drawing_spec,
                                              drawing_spec)

                    thumb_tip = hand_landmarks.landmark[self.mano.HandLandmark.THUMB_TIP]
                    index_finger_tip = hand_landmarks.landmark[self.mano.HandLandmark.INDEX_FINGER_TIP]
                    middle_finger_tip = hand_landmarks.landmark[self.mano.HandLandmark.MIDDLE_FINGER_TIP]
                    ring_finger_tip = hand_landmarks.landmark[self.mano.HandLandmark.RING_FINGER_TIP]
                    pinky_tip = hand_landmarks.landmark[self.mano.HandLandmark.PINKY_TIP]

                    fingers_vertical_pos = (thumb_tip.y + index_finger_tip.y + middle_finger_tip.y +
                                            ring_finger_tip.y + pinky_tip.y) / 5
                    fingers_horizontal_pos = (thumb_tip.x + index_finger_tip.x + middle_finger_tip.x +
                                            ring_finger_tip.x + pinky_tip.x) / 5

                    if all(tip.y > pinky_tip.y for tip in [thumb_tip, index_finger_tip, middle_finger_tip, ring_finger_tip]):
                        cv2.putText(image, 'Mano cerrada', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        self.V.model.hero.putBomb(self.V.model, time)
                    elif fingers_vertical_pos < thumb_tip.y or (pygame.event.get(pygame.KEYDOWN) and pygame.key.get_pressed()[pygame.K_UP]):
                        cv2.putText(image, 'Dedos arriba o boton arriba', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        self.V.model.hero.move(self.V.model, 0, 1)
                    elif fingers_vertical_pos > pinky_tip.y or (pygame.event.get(pygame.KEYDOWN) and pygame.key.get_pressed()[pygame.K_DOWN]):
                        cv2.putText(image, 'Dedos abajo o boton abajo', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        self.V.model.hero.move(self.V.model, 0, -1)
                    elif fingers_horizontal_pos < thumb_tip.x or (pygame.event.get(pygame.KEYDOWN) and pygame.key.get_pressed()[pygame.K_LEFT]):
                        cv2.putText(image, 'Dedos a la derecha o boton derecha', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),2)
                        self.V.model.hero.move(self.V.model, 1, 0)
                    elif fingers_horizontal_pos > pinky_tip.x or (pygame.event.get(pygame.KEYDOWN) and pygame.key.get_pressed()[pygame.K_RIGHT]):
                        cv2.putText(image, 'Dedos a la izquierda o boton izquierda', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),2)
                        self.V.model.hero.move(self.V.model, -1, 0)

                pygame.display.flip()  # actualizar pantalla
                pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps
                self.V.update()

            cv2.imshow('camara', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        pygame.time.wait(2000)
        pygame.quit()


'''
    def update(self):
        run = True
        while run:
            time = int(pygame.time.get_ticks() / 1000)

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
'''

