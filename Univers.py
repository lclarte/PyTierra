from CPU import *
from Enregistrement import *

TAILLE_MEMOIRE = 500

class Univers:
	"Contient les CPU et le monde i.e les instructions a executer"
	cpu_actuel 	   = 0

	def __init__(s):
		#code temporaire
		ancetre = charger_genome('ancestor')
		s.memoire = ancetre + [None]*(TAILLE_MEMOIRE-len(ancetre))
		s.liste_cpus 	= []

	def executer_cpus(s):
		"Cette fonction execute tous les CPU 1 fois\
		PRECISION IMPORTANTE : on parcourt la liste dans l'ordre des indices decroissant"
		cpu_depart = (s.cpu_actuel) #Contient le cpu auquel on devra s'arreter
		s.executer_cpu(s.cpu_actuel)
		s.next_cpu()
		while s.cpu_actuel != cpu_depart:
			s.executer_cpu(s.cpu_actuel)
			s.next_cpu()

	def executer_cpu(s, cpu): 
		"Execute le CPU actuellement pointe SANS PASSER AU SUIVANT\
		i.e sans incrementer cpu_actuel"
		s.liste_cpus[cpu].execute()


	def tuer_cpu(s, cpu):
		s.liste_cpus.remove(cpu)

	def tuer_cpu_actuel(s):
		liste.pop(s.cpu_actuel)

	def next_cpu(s):
		"Met a jour cpu_actuel pour pointer le suivant a executer"
		s.cpu_actuel = (s.cpu_actuel - 1) % len(s.liste_cpus)

	def inserer_cpu(s, ptr):
		"Insere un nouveau CPU dans la liste juste apres celui actuellement pointe"
		s.liste_cpus.insert(s.cpu_actuel+1, CPU(ptr, s))
