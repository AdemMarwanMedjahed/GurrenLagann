class Point(object):
    """Classe definissant un point dans un espace 3D"""
    def __init__(self, x, y, z):
        """Initialise les coordonnees du point """
        self.x=x
        self.y=y
        self.z=z

    def setPosition(self, point):
        """Modifie les coordonnees du point """
        if issubclass(type(point), Point):
            self.x=point.x
            self.y=point.y
            self.z=point.z
    
    def deplacer(self, vecteur):
        """Deplace le point d'un vecteur (dx, dy, dz)"""
        if issubclass(type(vecteur),Point) and vecteur:
            self.x=self.x+vecteur.x
            self.y=self.y+vecteur.y
            self.z=self.z+vecteur.z

    def __repr__(self):
        """Quand on entre un objet3D dans l'interpreteur"""
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __getattr__(self, nom):
        """Permet d'acceder a un attribut. si ce n'est pas possible:"""
        print("L'attribut {} n'est pas accessible dans Point !".format(nom))

    def __add__(self, point):
        if issubclass(type(point), Point) and point:
            return Point(self.x+point.x, self.y+point.y, self.z+point.z)
    
        
