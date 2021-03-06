from .Objet3D import  *
from .Polygone3D import *
from .Pave import *
from .pointDansPolygone import point_inside_polygon as pi
from math import *

class Arene(object):
    """
    Definit une structure de base pour une arene contenant des Objet3D
    """

    def __init__(self):
        """
        objets3D: [Objet3D]
        """
        self.objets3D = list()

    def add(self, objet3D):
        """
        Ajoute un objet3D a la liste si c'est une sous classe de Objet3D
        """
        if (issubclass(type(objet3D), Objet3D)):
            self.objets3D.append(objet3D)

    def vider(self):
        """
        Reinitialise la liste d'objets 3D
        """
        self.objets3D = list()


    def vueDessus(self, xmax, ymax):
        matrice2D = [[-1] * ymax for _ in range(xmax)]
        resolutionx = 0
        resolutiony = 0
        maximumx = xmax
        maximumy = ymax

        """On regarde combien de chiffres possede xmax et ymax pour determiner la resolution de la matrice"""
        while(maximumx):
            resolutionx += 1
            maximumx = maximumx/10
        while(maximumx):
            resolutiony += 1
            maximumy = maximumy/10

        for a in self.objets3D:
            if isinstance(a, Polygone3D):
                listeSommets = a.sommets
                if len(listeSommets) > 0 :
                    for i in range(0, xmax * (resolutionx*10)):
                        for j in range(0, ymax * (resolutionx*10)):
                            boolean = a.point_inside_polygon(i, j, listeSommets)
                            if(boolean):
                                matrice2D[i][j] = 1
                                print(boolean)
                            print(i, j)

    def sauvegarder(self, nomfichier):
        f = open(nomfichier , "w")
        f.write("1024 1024\n")
        for objet in self.objets3D:
            if issubclass(type(objet), Pave):
                f.write("PAVE {} {} {}".format(objet.longueur, objet.largeur, objet.hauteur))
            else:
                f.write("POLYGONE3D")
                for som in objet.sommets:
                    f.write(" ({},{},{})".format(som.x, som.y, som.z))
            f.write("\n")
        f.close()

    def lecture_fichier(self, fichier):
        mon_fichier = open(fichier, "r")
        for line in mon_fichier.read().splitlines()[1:]:
            words = line.split();
            if (words[0] == "POLYGONE3D"):
                polygone = Polygone3D()
                for sommet in words[1:]:
                    sommet_str = sommet.replace("(", "")
                    sommet_str = sommet_str.replace(")", "")
                    sommet_tab = sommet_str.split(",")
                    polygone.addSommet(Point(int(sommet_tab[0]), int(sommet_tab[1]), int(sommet_tab[2])))

                self.add(polygone)
            if (words[0] == "PAVE"):
                pave = Pave(int(words[1]),int(words[2]),int(words[3]))
                self.add(pave)
        mon_fichier.close()

    def __repr__(self):
        """
        Quand on entre une arene dans l'interpreteur
        """
        return "Arene: objets3D({})".format(self.objets3D)

    def __getattr__(self, nom):
        """
        Permet d'acceder a un attribut

        si ce n'est pas possible:
        """
        print("L'attribut {} n'est pas accessible dans Arene !".format(nom))

    def vueDessus(self, xmax, ymax):
        matrice2D = [['.'] * ymax for _ in range(xmax)]
        resolutionx = 1
        resolutiony = 1
        boolean = False

        """On regarde combien de chiffres possede xmax et ymax pour determiner la resolution de la matrice"""
        for ob in self.objets3D :
            if ob.centre.x > resolutionx :
                resolutionx = ob.centre.x
            if ob.centre.y > resolutiony :
                resolutiony = ob.centre.y
        if resolutiony == 1 :
            resolutiony = ymax
        if resolutionx == 1 :
            resolutionx = xmax

        for a in self.objets3D:
            if isinstance(a, Pave):
                listeSommets = a.sommets
                for i in range(int(listeSommets[0].x), int(listeSommets[3].x) + 1):
                    for j in range(int(listeSommets[0].y), int(listeSommets[3].y) + 1):
                        boolean = pi(i, j, listeSommets)
                        if(boolean):
                                    matrice2D[int(i*xmax / resolutionx)][int(j*ymax / resolutiony)] = 1


        return matrice2D

    def vueDessus2(self, high , width) :
        matrice2D = [['.'] * (int(high+high/2)) for _ in range(int( width + width/2))]
        j = 1
        for obj in self.objets3D :
            if issubclass(type(obj) ,Pave) :
                for i in range(0 , 4) :
                    pointA = obj.sommets[i]
                    pointB = obj.sommets[j]
                    segment = Vecteur(pointB.x - pointA.x , pointB.y - pointA.y , 0)
                    if pointB.x == pointA.x :
                        angle = pi / 2
                    elif pointB.y == pointA.y :
                        angle = 0.0
                    else :
                        angle = segment.getAngle2D()
                    print(pointA.x , pointB.x)
                    for x in range(int( min(pointA.x , pointB.x) + width / 2 ) ,int ( max(pointB.x , pointA.x) + width / 2 )  ) :
                        matrice2D[int(x)][int( (x - pointA.x - width/2) * tan(angle)  + high/2 + pointA.y)] = i
                        matrice2D[int(x)][int( (x - pointA.x - width /2) * tan(angle) + high / 2 + pointA.y) -1] = i
                    for y in range(int( min(pointA.y , pointB.y) + high/2 ) ,int ( max(pointB.y , pointA.y) + high/2  )) :
                        matrice2D[int( (y - pointA.y - high/2)/tan(angle)  + width/2 + pointA.x )][int(y)] = i
                        matrice2D[int( (y - pointA.y - high/2) / tan(angle) + width / 2 + pointA.x) - 1 ][int(y)] = i

                    j += 1
                    if j == 4 : j = 0


        return matrice2D