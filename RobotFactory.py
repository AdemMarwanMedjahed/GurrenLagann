import Robot, Roue, Moteur,Tete, CapteurDistance,Accelerometre,Camera, Arene.Point, Arene.Vecteur, Arene.Objet3D


class RobotFactory(object):
    """classe usine (de parametrage) pour faciliter la creation du robot"""


    def make(self, position, long, larg):
        """position initiale du robot long et larg sont les dimentions du robot à modifier si necessaire"""
        x=position._x
        y=position._y
        direction=Vecteur(0,0,0)

        forme=Objet3D()
        a=Point(x-larg/2,y+long/2,0)
        b=Point(x+larg/2,y+long/2,0)
        c=Point(x+larg/2,y-long/2,0)
        d=Point(x-larg/2,y-long/2,0)
        forme.addSommet(a)
        forme.addSommet(b)
        forme.addSommet(c)
        forme.addSommet(d)
        #pour definir un rectangle de centre "position" a corespont au point en haut a droite
        #les suivants dans le sens des aiguilles d'une montre

        m1=Moteur(260) #vitesse max à modifier
        m2=Moteur(260)

        rd=Roue(b,3,m1)
        rg=Roue(a,3,m2)

        cpdist=CapteurDistance()
        acc=Accelerometre()
        cam=Camera()
        lstcap=list()
        lstcap.append(cpdist)
        lstcap.append(cam)
        lstcap.append(acc)

        tete=Tete(Point(x,y+long/2,0),direction,lstcap)

        robot=Robot(position, direction, forme, tete, rg, rd)

        return robot


