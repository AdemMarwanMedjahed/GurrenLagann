from Arene.Point import *
from math import *
from Arene.fonctions import atan2

class Vecteur(Point):
    """Defini des methodes de calcul sur les vecteurs"""
    # - __errNorme : lors de la rotation2D, si la norme du vecteur est diminuee, on enregistre l'ecart dans cette variable
    SEUIL_ERR = 1
    
    def __init__(self, x, y, z):
        """Constructeur qui intialise les coordonnees et l'erreur en norme de la methode rotation2D """
        Point.__init__(self,x,y,z)
        self.__errNorme=0.0
        
    def __mul__(self, vecteur):
        """ produit scalaire"""
        if issubclass(type(vecteur), Vecteur) and vecteur:
            return self.x*vecteur.x+self.y*vecteur.y+self.z*vecteur.z

    def __pow__(self, vecteur):
        """produit vectoriel """
        if issubclass(type(vecteur), Vecteur) and vecteur:
            return Vecteur(self.y*vecteur.z-self.z*vecteur.y, self.z*vecteur.x-self.x*vecteur.z, self.x*vecteur.y-self.y*vecteur.x)

    def __add__(self, vecteur):
        """ addition"""
        if issubclass(type(vecteur), Vecteur) and vecteur:
            return Vecteur(self.x+vecteur.x, self.y+vecteur.y, self.z+vecteur.z)

    def getAngle2D(self):
        """ Retourne l'angle du vecteur par rapport a la verticale, dans le sens trigo, entre pi et -pi"""
        return self.diffAngle2D(Vecteur(1,0,0))
    
    def diffAngle2D(self, vecteur):
        """retourne la difference d'angle entre 2 vecteurs dans le repere (x, y) """
        if issubclass(type(vecteur), Vecteur) and vecteur:
            # v: self^vecteur
            v=self**vecteur
            if self.y != 0 and vecteur.x != 0:
                #utilise les proprietes du produit vectoriel pour determiner si l'angle est positif ou negatif
                if v.z>0:
                    return -acos((self*vecteur)/(self.getNorme()*vecteur.getNorme()))
                elif v.z<0:
                    return acos((self*vecteur)/(self.getNorme()*vecteur.getNorme()))
            return atan2(vecteur.y, vecteur.x)-atan2(self.y, self.x)
                
    def getNorme(self):
        """Retourne la norme du vecteur """
        return sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))
    
    def rotation2D(self, teta):
        """tourne le vecteur d'un angle teta"""
        """pour tourner d'un angle teta, il vaut mieux que la norme du vecteur soit > a 2.pi/teta environ (pour une bonne precision sur les coordonnees)"""
        # n: norme
        # x: copie de self._x
        n=sqrt(pow(self.x,2)+pow(self.y,2))
        x=self.x
        
        self.x=(int)(x*cos(teta)-self.y*sin(teta))
        self.y=(int)(x*sin(teta)+self.y*cos(teta))
        n2=sqrt(pow(self.x,2)+pow(self.y,2))
        
        self.__errNorme=self.__errNorme+n-n2
        
        #si on s'est trop eloigne de la norme d'origine (selon x et y):
        if self.__errNorme>self.SEUIL_ERR:
            #ajustement de la norme
            a=self.getAngle2D()
            self.x=(int)((n2+self.__errNorme)*cos(a))
            self.y=(int)((n2+self.__errNorme)*sin(a))
            self.__errNorme=self.__errNorme-(sqrt(pow(self.x,2)+pow(self.y,2))-n2)
