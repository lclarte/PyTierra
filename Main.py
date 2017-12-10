import os 
import Univers
from CPU import *

class Main:

	def test(self):
		self.U.liste_cpus[0].afficher_etat()
		print(' ')
		print(' NB DE CPU :', len(self.U.liste_cpus))

	def __init__(self):
		i = 0
		self.U = Univers.Univers()
		self.U.inserer_cpu(0) #initialiste un CPU au debut de l'univers
		for i in range(800):
			self.U.executer_cpus()

		while True:
			os.system('clear')
			self.test()
			self.U.executer_cpus()
			s = raw_input()
			if s == "q":
				break
			if s == "d":
				print(self.U.memoire[0:10])
				print(self.U.memoire[47:51])
				raw_input()

Main()