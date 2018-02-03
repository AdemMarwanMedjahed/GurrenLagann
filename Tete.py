from Arene.Vecteur import *


class Tete(object):
    def __init__(self, position, direction, listeCapteurs):
        """positiont est de type point sont les coordonees de la tete et donc des capteurs"""
        """pareil pour direction"""
        """listeCapteur est la liste des capteurs pésents sur la tete"""
        self.position=position
        self.direction=direction
        self.listeCapteurs=list()

    def tourner(self, angle):
        self.direction.rotation2D(angle)

    def addCapteur(self, capt):
        self.listeCapteurs.append(capt)