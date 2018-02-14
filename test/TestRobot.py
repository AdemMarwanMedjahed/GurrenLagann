import unittest
from robotRep import Robot
from geometrie3D import Pave, Objet3D
from geometrie3D.pointRep import Vecteur


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.r = Robot(Pave(50, 50, 0), Objet3D(), Objet3D(), Vecteur(0, -1, 0))

    def test_initialisation(self):
        self.assertIsInstance(self.r, Robot, msg=None)
        self.assertIsInstance(self.r.rd, Objet3D, msg=None)
        self.assertIsInstance(self.r.rg, Objet3D, msg=None)
        self.assertIsInstance(self.r.forme, Pave, msg=None)
        self.assertIsInstance(self.r.direction, Vecteur, msg=None)

    def test_avancer(self):
        self.r.avancer()
