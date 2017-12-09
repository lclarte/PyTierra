from Instructions_Tierra import *

TAILLE_STACK = 10

class CPU:

	#ptr stocke l'adresse actuellement pointee par le CPU
	def __init__(self, ptr, univers):
		self.ax = self.bx = self.cx = self.dx = 0
		self.ptr							  = ptr
		self.univers						  = univers
		self.stack 							  = [0]*TAILLE_STACK
		self.stack_ptr						  = 0

	def execute(self):
		"execute l'instruction actuellement pointee par le CPU puis passe a la suivante\
		Attention, les instructions dans l'univers sont stockees sous forme de chaine de caractere\
		correspondant EXACTEMENT au nom des fonctions"
		try:
			f = eval(self.univers.memoire[self.ptr])
			f(self)
		except Exception as e:
			print(e)
		finally:
			self.incrementer_ptr()

	def incrementer_ptr(self):
		self.ptr = (self.ptr + 1)%(len(self.univers.memoire))

	def incrementer_stack_ptr(self):
		self.stack_ptr = (self.stack_ptr + 1) % (TAILLE_STACK)

	def decrementer_stack_ptr(self):
		self.stack_ptr = (self.stack_ptr + 1) % (TAILLE_STACK)

	def pop_stack(self):
		"Retourne la valeur du stack actuellement pointee SANS DECREMENTER\
		le stack pointeur"
		return self.stack[self.stack_ptr]

	def push_stack(self, x):
		"Met la valeur de l'argument dans la stack SANS INCREMENTER le stack\
		pointeur"
		self.stack[self.stack_ptr] = x

	def die(self):
		univers.kill(self)

	#FONCTIONS D'AFFICHAGE
	def afficher_etat(self):
		print("valeurs de ax, bx, cx et dx : ")
		print(self.ax, self.bx, self.cx, self.dx)
		print("Etat du pointeur d'instructions")
		print(self.ptr, " sur ", self.univers.memoire[self.ptr])