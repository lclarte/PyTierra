import Univers
import CPU
import random
from Utilitaire import *
import math

LIMITE_RECHERCHE = 10

#Definit la limite de recherhe pour le template
longueur_pattern = 0

def nop0(cpu):
	pass

def nop1(cpu):
	pass

def not0(cpu):
	if cpu.cx % 2 == 0:
		cpu.cx += 1
	else:
		cpu.cx -= 1

def shl(cpu):
	cpu.cx << 1

def zero(c):
	c.cx = 0
	c.incrementer_ptr() #cf doc tierra p 278

def ifz(c):
	#Si cx vaut 0, on ne fait rien car le CPU va ensuite de lui 
	#meme incrementer son ptr
	if c.cx != 0:
		c.incrementer_ptr()

def subCAB(c):
	c.cx = c.ax - c.bx

def subAAC(c):
	c.ax = c.ac - c.cx

def incA(c):
	c.ax += 1

def incB(c):
	c.bx += 1

def incC(c):
	c.cx += 1

def incD(c):
	c.dx += 1

def decA(c):
	c.ax -= 1

def decB(c):
	c.bx -= 1

def decC(c):
	c.cx -= 1

def decD(c):
	c.dx -= 1

def pushA(c):
	c.push_stack(c.ax)
	c.incrementer_stack_ptr()

def pushB(c):
	c.push_stack(c.bx)
	c.incrementer_stack_ptr()

def pushC(c):
	c.push_stack(c.cx)
	c.incrementer_stack_ptr()

def pushD(c):
	c.push_stack(c.dx)
	c.incrementer_stack_ptr()

def popA(c):
	c.ax = c.pop_stack()
	c.decrementer_stack_ptr()

def popB(c):
	c.bx = c.pop_stack()
	c.decrementer_stack_ptr()

def popC(c):
	c.cx = c.pop_stack()
	c.decrementer_stack_ptr()

def popD(c):
	c.dx = c.pop_stack()
	c.decrementer_stack_ptr()

def jmp(c):
	l_pattern, indice_avant, i_avant = trouver_template_complementaire_avant(c, LIMITE_RECHERCHE)
	l_pattern_arriere, indice_arriere, i_arriere = trouver_template_complementaire_arriere(c, LIMITE_RECHERCHE)
	if indice_arriere == indice_avant == -1:
		raise Exception("Pattern non trouve")
		return
	else:
		if i_avant < i_arriere or indice_arriere == -1:
			c.ptr = indice_avant
		else:
			c.ptr = indice_arriere
			print(l_pattern, indice_arriere, i_arriere)
	c.ptr -= 1#Car apres l'execution, on fait faire c.ptr += 1
	#donc on compense pour pas  sauter le premier nop du pattern trouve

def jmpb(c):
	l_pattern, indice_arriere, i_arriere = trouver_template_complementaire_arriere(c, LIMITE_RECHERCHE)
	if indice_arriere == -1:
		raise Exception("Pattern non trouve")
	else:
		c.ptr = indice_arriere
	c.ptr -= 1

def call(c):
	l_pattern, indice_avant, i_avant = trouver_template_complementaire_avant(c, LIMITE_RECHERCHE)
	l_pattern_arriere, indice_arriere, i_arriere = trouver_template_complementaire_arriere(c, LIMITE_RECHERCHE)
	if l_pattern == 0:
		c.push_stack(c.ptr +1)
	if indice_arriere == indice_avant == -1:
		c.ptr = c.ptr + l_pattern + 1
		raise Exception("Pattern non trouve")
		return
	else:
		if i_avant < i_arriere or indice_arriere == -1:
			c.ptr = indice_avant
			c.push_stack(indice_avant)
		else:
			c.ptr = indice_arriere
			c.push_stack(indice_avant)
def ret(c):
	x = c.pop_stack()
	c.decrementer_stack_ptr()
	c.ptr = x

def movDC(c):
	c.dx = c.cx

def movBA(c):
	c.bx = c.ax

def adr(c):
	pass

def adrb(c):
	pass

def adrf(c):
	pass

#													NOUVELLES INSTRUCTIONS
def new(c):
	"Creer un nouveau cpu a l'endroit de ax"
	c.univers.inserer_cpu(c.ax)

def rand(c):
	c.ax  = int(Univers.TAILLE_MEMOIRE*random.random())
	"Place dans c.ax une valeur aleatoire"

def read(c):
	"Lit l'instruction correspondant a l'adresse presente dans c.bx et la place dans la stack"
	c.push_stack(c.univers.memoire[c.bx])
	c.incrementer_stack_ptr()

def write(c):
	"Ecrit l'instruction au sommet de la pile dans l'adresse contenue dans c.ax"
	c.univers.memoire[c.ax] = c.pop_stack()
	c.decrementer_stack_ptr()