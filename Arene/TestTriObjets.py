from Arene import *
from Objet3D import *
from Point import *
from TriObjets import *


#Creation d'une arene et ajout de n objets
a=Arene()

o1=Object3D()
	
o1.addSommet(Point (randint(200,300),randint(200,300),randint(200,300)) )
o1.addSommet(Point (randint(200,300),randint(200,300),randint(200,300)) )
o1.addSommet(Point (randint(200,300),randint(200,300),randint(200,300)) )
o1.addSommet(Point (randint(200,300),randint(200,300),randint(200,300)) )

o1.setCentre(Point (randint(200,300),randint(200,300),randint(200,300)) )
	
o2.Object3D()
	
o2.addSommet(Point (randint(100,200),randint(100,200),randint(100,200)) )
o2.addSommet(Point (randint(100,200),randint(100,200),randint(100,200)) )
o2.addSommet(Point (randint(100,200),randint(100,200),randint(100,200)) )
o2.addSommet(Point (randint(100,200),randint(100,200),randint(100,200)) )

o2.setCentre(Point (randint(100,200),randint(100,200),randint(100,200)) )

o3.Object3D()
	
o3.addSommet(Point (randint(0,100),randint(0,100),randint(0,100)) )
o3.addSommet(Point (randint(0,100),randint(0,100),randint(0,100)) )
o3.addSommet(Point (randint(0,100),randint(0,100),randint(0,100)) )
o3.addSommet(Point (randint(0,100),randint(0,100),randint(0,100)) )

o3.setCentre(Point (randint(0,100),randint(0,100),randint(0,100)) )

a.Objets3D.append(o3)
a.Objets3D.append(o2)
a.Objets3D.append(o1)

print("affichage de la liste d'objets non triée \n")
print(a.Objets3D)
triObjets(a)
print("affichage de la liste d'objets triée \n")
print(a.Objets3D)


