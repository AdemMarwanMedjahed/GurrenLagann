from geometrie3D.pointRep import Vecteur
from geometrie3D import Objet3D

class Robot(Objet3D):
    """
    Classe definissant les elements essentiels d'un robot
    """
    def __init__(self, pave, rg, rd, direction):
        """
        
        Constructeur du robot
        
        direction: Vecteur norme montrant la direction initiale du robot
        forme: Pave attendu (correspond aux methodes de deplacement)
        rd: Objet3D, roue droite
        rg: Objet3D, roue gauche
        """
        Objet3D.__init__(self)
        self.direction=direction
        self.vitesse=0.0
        self.vitesseRot=0.0
        self.forme=pave
        self.centre=pave.centre #initalise le centre au centre du pave
        self.rd=rd
        self.rg=rg
        
        #initialisation des centres des roues
        self.rd.centre=pave.sommets[1]/2
        self.rg.centre=pave.sommets[0]/2        

    def avancer(self, sens):
        """
        deplace le robot dans le sens voulu (1 pour l'avant, -1 pour l'arriere par ex), sur sa direction
        """
        if sens<0:
            self.deplacer(self.direction*-self.vitesse)
        elif sens>0:
            self.deplacer(self.direction*self.vitesse)

    def tourner(self, sens):
        """
        tourne le robot par rapport a une des roues selon le sens 
        """
        if sens<0:
            self.direction.rotation2D(self.vitesseRot)
            self.tournerAutour(self.rd.centre, self.vitesseRot)
        elif sens>0:
            self.direction.rotation2D(-self.vitesseRot)
            self.tournerAutour(self.rg.centre, -self.vitesseRot)
    
    def tournerAutour(self, point, angle):
        """
        tourne le robot autour de point d'un angle teta
        """
        #rotation du pave et des roues
        self.forme.tournerAutour(point, angle)
        self.rg.centre.tournerAutour(point, angle)
        self.rd.centre.tournerAutour(point, angle)
            
    def deplacer(self, vecteur):
        """
        deplace le corps et les roues du robot
        """
        self.forme.deplacer(vecteur)
        self.rg.deplacer(vecteur)
        self.rd.deplacer(vecteur)






