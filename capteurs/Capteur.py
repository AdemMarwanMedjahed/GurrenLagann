from composants.Tete import *


class Capteur(object):

    def __init__(self, type, tete):
        """position est de type Point ce sont les coordonees du capteur"""
        """direction est de type Vecteur est la direction vers laquelle pointe le capteur"""
        """type est un string decrivant la nature du capteur (distance, camera ou accelerometre)"""
        """la position et la direction des capteurs sont les memes que celles de la tete"""
        self.position=tete.position
        self.direction=tete.direction
        self.type=type

