


class Moteur(object):
    def __init__(self, vitesseMax):
        """vitesseMax est la vitesse maximale du moteur"""
        """sens de type string est le sens de rotation du moteur vers l'avant ou vers l'arierre"""
        """vitesseCourante est la vitesse en temps reel du moteur"""

        self.vitesseMax=vitesseMax
        self.sens="avant"
        self.vitesseCourante=0

    def demarrer(self, vitesse, temps):
        if(vitesse < self.vitesseMax):
            t=0
            while(t<temps):
                self.vitesseCourante=vitesse
                t+=1

        self.vitesseCourante=0
        nombreTours=vitesse*temps
        return nombreTours

    def arreter(self):
        self.vitesseCourante=0




