from robotRep.Capteur import Capteur
from math import sqrt, pow, fabs
from geometrie3D.pointRep.Vecteur import *


class Accelerometre(Capteur):

    def __init__(self, position):
        """position doit etre initialisé a la position du robot !
         (qui est constament mise a jour lors du déplacement)
        type est un string pour distinguer l'accelero des autres capteurs
           state est un booleen qui represente l'etat du capteur on/off"""
        Acelerometre.temps=0
        Capteur.__init__(position, Vecteur(0,0,0))
        self.type="accelerometre"
        self.state= True
        self.FPS=0.5#pas mettre a 0
        self.vitesseVectorielle=Vecteur(0,0,0)
        self.accelerationVectorielle=Vecteur(0,0,0)

    def start(self):
        self.state=True

    def stop(self):
        self.state=False

    def setTimeSensitivity(self, dt):
        self.dt=dt

    def getVectSpeed(self):
        return self.vitesseVectorielle

    def getVectAcc(self):
        return self.accelerationVectorielle

    def getSpeedValue(self):
        return sqrt(pow(self.vitesseVectorielle.x,2)+pow(self.vitesseVectorielle.y,2)+pow(self.vitesseVectorielle.z,2))

    def getAccValue(self):
        return sqrt(pow(self.accelerationVectorielle.x,2)+pow(self.accelerationVectorielle.y,2)+pow(self.accelerationVectorielle.z,2))

    def getPos(self):
        return self.position

    def accUpdate(self):
        """vérifie la position du robot toute les dt secondes
        et en déduit la vitesse et l'acceleration du robot selon les 3 axes X Y Z"""

        self.start()
        while(self.state):
            if(not self.state):
                break

            a=Robot.getPositionCourante()
            va=self.vitesseVectorielle

           # creer un temps d'attente suffisant pour permettre l'avancee du robot
           time.sleep(self.FPS)
           
           b=Robot.getPositionCourante()
          # vb=self.vitesseVectorielle
           
           dx=fabs(b.x-a.x)
           dy=fabs(b.y-a.y)
           dz=fabs(b.z-a.z)
           self.vitesseVectorielle=Vecteur(dx/self.FPS,dy/self.FPS,dz/self.FPS) #utilite de cacluler vitesseVectorielle si on l a deja au dessus
           #time.sleep(dt) on discretise le dt =1
           vb=self.vitesseVectorielle
           dvx=vb.x-va.x
           dvy=vb.y-va.y
           dvz=vb.z-va.z
           self.accelerationVectorielle=Vecteur(dvx/self.FPS,dvy/self.FPS,dvz/self.FPS)
     

