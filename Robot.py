from composants.Roue import *
from composants.Tete import *
from math import pi
from Arene.Vecteur import *
from Arene.Point import *
from Arene.Objet3D import *



class Robot(object):
    def __init__(self, position, direction, forme, tete, rg, rd):
        """position est de type Point c'est le centre du robot"""
        """direction est le vecteur direction du robot de type Vecteur"""
        """forme est la forme geometrique du robot de preferance rectangulaire de type Objet3D"""
        """tete est la tourelle sur laquelle sont montées les capteurs un type a part"""
        """rg et rd sont les roues du robot respectivement gauche et droite d type Roue"""
        self.position=position
        self.direction=direction
        self.forme=forme
        self.tete=tete
        self.rg=rg
        self.rd=rd

    def avancer(self, distance, vitesse, direction):
        #v est le vecteur de déplacement selon la direction et sa norme est distance
        v=Vecteur(direction.x*distance, direction.y*distance,0)
        self.direction=direction
        self.rd.tourner(distance / self.rd.rayon * 2 * pi, vitesse)
        self.rg.tourner(distance / self.rg.rayon * 2 * pi, vitesse)
        self.position.deplacer(v)
        self.forme.deplacer(v)

    def tournerTete(self, angle):
        self.tete.tourner(angle)

    def rotation(self, angle, axe):
        angle=angle*pi/180
        for sommet in self.forme.getSommets():
            v=Vecteur(sommet.x-axe.x,sommet.y-axe.y,0)
            v.rotation2D(angle)
            sommet.x=v.x
            sommet.y=v.y

    def toString(self):
        for sommet in self.forme.getSommets():
            print("("+str(sommet.x)+","+str(sommet.y)+")",end="   ")










