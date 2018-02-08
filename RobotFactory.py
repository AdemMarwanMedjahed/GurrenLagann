from Robot import *
from composants.Roue import *
from composants.Moteur import *
from composants.Tete import *
from capteurs.CapteurDistance import *
from capteurs.Accelerometre import *
from capteurs.Camera import *
from Arene.Vecteur import *
from Arene.Point import *
from Arene.Objet3D import *


class RobotFactory(object):
    """classe usine (de parametrage) pour faciliter la creation du robot"""

    @staticmethod
    def make(position, long, larg):
        """position initiale du robot long et larg sont les dimentions du robot à modifier si necessaire"""
        x = position.x
        y = position.y
        direction = Vecteur(0, 0, 0)

        forme = Objet3D()
        a = Point(x - larg / 2, y + long / 2, 0)
        b = Point(x + larg / 2, y + long / 2, 0)
        c = Point(x + larg / 2, y - long / 2, 0)
        d = Point(x - larg / 2, y - long / 2, 0)
        forme.addSommet(a)
        forme.addSommet(b)
        forme.addSommet(c)
        forme.addSommet(d)
        # pour definir un rectangle de centre "position" a corespont au point en haut a droite
        # les suivants dans le sens des aiguilles d'une montre

        m1 = Moteur(260)  # vitesse max à modifier
        m2 = Moteur(260)

        rd = Roue(b, 3, m1)
        rg = Roue(a, 3, m2)

        tete = Tete(Point(x, y + long / 2, 0), direction)

        cpdist = CapteurDistance(tete)
        acc = Accelerometre(tete)
        cam = Camera(tete)
        lstcap = list()
        lstcap.append(cpdist)
        lstcap.append(cam)
        lstcap.append(acc)

        robot = Robot(position, direction, forme, tete, rg, rd)

        return robot


pos = Point(0, 0, 0)
dir = Vecteur(1, 0, 0)
rob = RobotFactory.make(pos,10,5)
rob.toString()
print("\n----------avancer----------")
rob.avancer(0.5,10,dir)
rob.toString()
print("\n----------rotation----------")
rob.rotation(90,pos)
rob.toString()