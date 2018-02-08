from capteurs.Capteur import *
from Arene.Arene import *

class CapteurDistance(Capteur):
    def __init__(self, tete):
        Capteur.__init__(self,"distance",tete)

    #def getDistance(self):