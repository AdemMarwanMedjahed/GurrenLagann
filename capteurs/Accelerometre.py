from Robot import *
from capteurs.Capteur import *


class Accelerometre(Capteur):
    def __init__(self, tete):
        Capteur.__init__(self,"accelerometre", tete)

    #def getAcceleration(self):
