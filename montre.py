#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading

class Clock(threading.Thread):
	def __init__(self, h, m, s, form):
		threading.Thread.__init__(self)
		assert isinstance (form, bool)
		self.form = form
		if (self.form == True):
			#On vérifie que l'affichage correspond à un format 12h si self.form = true
			assert isinstance (h, int) and (h <= 12) and (h >= 0)
		elif(self.form == False):
			#On vérifie que l'affichage correspond à un format 24h si self.form = false
			assert isinstance (h, int) and (h <= 24) and (h >= 0)
		else:
			print("Erreur: le booléen pose problème.")#message de debug 1
		assert isinstance (m, int) and (m <= 60)
		assert isinstance (s, int) and (s <= 60)
		self.h = h
		self.m = m
		self.s = s
		print("Init time is :  {}:{}:{}\n".format(self.h, self.m, self.s))
	
	def run(self):
		if(self.form == False):
			while True:#boucle infinie
				while(self.h <= 24):#boucle des heures
					while(self.m < 60):#boucle des minutes
						while (self.s < 60):#boucle des secondes
							self.s += 1
							time.sleep( 1 )#Partie compteur
							print("time is : {}:{}:{}".format(self.h, self.m, self.s)) #Affichage de l'heure
						#Les 5 lignes font la transition vers l'unité supérieure, ainsi qu'un reset de l'unité inférieur
						self.s = 0
						self.m += 1
					self.m = 0
					self.h +=1
				self.h = 1
				print("Un jour de plus")
		elif(self.form == True):
			while True:#boucle infinie
				while(self.h <= 12):#boucle des heures
					while(self.m < 60):#boucle des minutes
						while (self.s < 60):#boucle des secondes
							self.s += 1
							time.sleep( 1 )#Partie compteur
							print("time is : {}:{}:{}".format(self.h, self.m, self.s)) #Affichage de l'heure
						#Les 5 lignes font la transition vers l'unité supérieure, ainsi qu'un reset de l'unité inférieur
						self.s = 0
						self.m += 1
					self.m = 0
					self.h +=1
				self.h = 1
				print("Un jour de plus")
		else:
			print("Encore un problème de booléen")#message de debug 2


# test()
heure = Clock(6, 22, 00, True)#false -> format 24h / true -> format 12h 
heure.start()