from Univers import *
import math 

def knuth_morris_pratt(s, t):
	"Retourne l'indice a partir duquel commence la sous chaine t dans s"
	#s est la "grande" chaine de caractere, t est le motif a trouver
	assert t != ' '
	len_s = len(s)
	len_t = len(t)
	r = [0]*len_t
	j = r[0] = -1
	for i in range(1, len_t):
		while j >= 0 and t[i-1] != t[j]:
			j = r[j]
		j += 1
		r[i] = j
	j = 0
	for i in range(len_s):
		while j >= 0 and s[i] != t[j]:
			j = r[j]
		j += 1
		if j == len_t:
			return i - len_t + 1
	return -1

def calculer_pattern(memoire, ptr_tmp):
	"Calcule la suite de nop complemtaire a celle debutant en ptr_tmp"
	pattern = [] #on rappelle que le pattern qu'on cherche est 
	#le COMPLEMENTAIRE de celui qu'on voit
	while True:
		if memoire[ptr_tmp] == "nop0":
			pattern.append("nop1")
		elif memoire[ptr_tmp] == "nop1":
			pattern.append("nop0")
		else:
			break
		ptr_tmp = (ptr_tmp + 1) % len(memoire)
	return pattern

def trouver_template_complementaire_avant(c, LIMITE_RECHERCHE):
	return trouver_template_complementaire_avant_mem(c.univers.memoire, c.ptr, LIMITE_RECHERCHE)

def trouver_template_complementaire_avant_mem(memoire, ptr, LIMITE_RECHERCHE):
	"Renvoie la longueur du pattern qui suit l'instruction, et renvoie l'adresse\
	qui demarre le pattern complementaire i.e la premiere instruction du pattern\
	ou c.ptr + 1 dans le cas ou le pattern est vide ou n'a pas ete trouve.\
	On renvoie aussi i qui est le temps pris pour trouver le pattern"
	#c est le CPU
	pattern = calculer_pattern(memoire, ptr + 1)
	longueur_pattern = len(pattern)
	if longueur_pattern == 0:
		return (0, ptr + 1, 0)
	copie_avant = memoire[ptr+longueur_pattern+1:] + memoire[:ptr]
	i 			= knuth_morris_pratt(copie_avant, pattern)
	
	#dans le cas ou on a rien trouve
	if i < 0:
		return (longueur_pattern, -1, float('inf'))

	indice_reel = 0
	if i >= (len(memoire)-(ptr+longueur_pattern+1)):
		indice_reel = i - (len(memoire)-(ptr+longueur_pattern+1))
	else:
		indice_reel = i + ptr + longueur_pattern + 1
	#Pour l'instant, on s'en fout de LIMITE RECHERCHE
	return (longueur_pattern, indice_reel, i) 

def trouver_template_complementaire_arriere(c, LIMITE_RECHERCHE):
	return trouver_template_complementaire_arriere_mem(c.univers.memoire, c.ptr, LIMITE_RECHERCHE)

def trouver_template_complementaire_arriere_mem(memoire, ptr, LIMITE_RECHERCHE):
	#c est le CPU
	pattern = calculer_pattern(memoire, ptr + 1)
	pattern_arriere = pattern[::-1]
	longueur_pattern = len(pattern)
	if longueur_pattern == 0:
		return (0, ptr + 1, 0)

	copie_avant = memoire[ptr+longueur_pattern+1:] + memoire[:ptr]
	copie_arriere = copie_avant[::-1]
	i 			  = knuth_morris_pratt(copie_arriere, pattern_arriere)
	
	#dans le cas ou on a rien trouve
	if i < 0:
		return (longueur_pattern, -1, float('inf'))
	
	indice_reel = 0
	#Le i est l'indice en sachant qu'on a commence a compter a partir de c.ptr - 1 
	if i >= ptr:
		indice_reel = (len(memoire) - i + (ptr-1) - longueur_pattern + 1)%(len(memoire))
	else:
		indice_reel =(ptr - i - longueur_pattern)%len(memoire)
	#Pour l'instant, on s'en fout de LIMITE RECHERCHE
	return (longueur_pattern, indice_reel, i)