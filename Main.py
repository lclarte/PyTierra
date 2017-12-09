import Univers
from CPU import *

class Main:

	def test(self):
		self.U.liste_cpus[0].afficher_etat()

	def __init__(self):
		self.U = Univers.Univers()
		self.U.inserer_cpu(0) #initialiste un CPU au debut de l'univers
		for i in range(100):
			self.U.executer_cpus()
			self.test()
			s = raw_input()
			if s == "q":
				break

Main()