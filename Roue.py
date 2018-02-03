from math import pi
import Moteur


class Roue(object):
    def __init__(self, posistion, rayon, moteur):
        """position est de type Point indique les coordonees de la roue"""
        """rayon est de type float cest le rayon de la roue"""
        self.position=posistion
        self.rayon=rayon
        self.moteur=moteur

    def tourner(self, nbTours, vitesse):
        dist=self.rayon*2*pi*nbTours #dist= perimetre du cercle * nbTours
        Moteur.demarrer(vitesse, dist/vitesse)

    def frener(self):
        Moteur.arreter()


