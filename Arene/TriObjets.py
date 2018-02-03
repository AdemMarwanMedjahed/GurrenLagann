
from Arene import *

#peut etre ajouté a Arene.py
def triObjects(self):
"""tri des Objets se trouvant dans une aréne en fonction de leurs hauteurs pour pouvoir les afficher correctement en 2D"""
	medHeight=list()
	zmax=0
	zmin=0

	#liste hauteurs d'objets
	for o in self.Objets3D:
		for s in o.sommets:
			if(s.z>zmax):
				zmax=s.z
			if(s.z<zmin):
				zmin=s.z
		medHeight.append((float(zmin+zmax))/2.0)


	i=0
	#tri des objets en fonction des hauteurs
	while(i<len(medHeight)-1):
		for j in range(i+1,len(medHeight)):
			if(medHeight[j]<medHeight[i]):
				tempI=medHeight[j]
				medHeight[j]=medHeight[i]
				medHeight[i]=tempI

				tempO=self.Object3D[j]
				self.Objets3D[j]=self.Objects3D[i]
				self.Objects3D[i]=tempO
		i=i+1
