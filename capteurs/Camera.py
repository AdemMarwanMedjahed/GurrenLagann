from  capteurs.Capteur import *


class Camera(Capteur):
    def __init__(self, tete):
        Capteur.__init__(self,"camera", tete)
