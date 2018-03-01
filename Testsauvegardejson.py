from geometrie3D import *
import filecmp


#Creation d'une arene et ajout de n objets
a = Arene()
poly = Polygone3D()
p = Pave(10, 10, 10)
#p.tournerAutour(Point(0,4,5) , pi/3)
poly.sommets = [Point(14, 15, 14), Point(5, 99, 120)]
#a.add(poly)
a.add(p)
a.add(poly)
b = Arene(list())
a.sauvegardeArenejson("sauvegarde_a.txt")
b = a.lireArenejson("sauvegarde_a.txt")
b.sauvegardeArenejson("sauvegarde_b.txt")
c = b.lireArenejson("sauvegarde_b.txt")
c.sauvegardeArenejson("sauvegarde_c.txt")


import filecmp
print(filecmp.cmp('sauvegarde_a.txt', 'sauvegarde_c.txt'))
