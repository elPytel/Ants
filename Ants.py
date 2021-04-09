# By Pytel

import random
import AntHill

DEBUG = True

class Ant:
	
	_MAX_WILL = 100		# 0 - 100%
	_MAX_EYESHOT = 3	# r - "radius"
	_MAX_TTL = 1000		# time to live
		
	def __init__ (self, will = -1, eye = -1, ttl = -1):
		if will == -1:
			self.will = round(random.gauss(Ant._MAX_WILL/2, Ant._MAX_WILL/4))
			if self.will < 0:
				self.will = 0
			elif self.will > Ant._MAX_WILL:
				self.will = Ant._MAX_WILL
		else:
			self.will = will
		
		if eye == -1:
			self.eye = round(random.gauss(Ant._MAX_EYESHOT/2, Ant._MAX_EYESHOT))
			if self.eye < 1:
				self.eye = 1
			elif self.eye > Ant._MAX_EYESHOT:
				self.eye = Ant._MAX_EYESHOT
		else:
			self.eye = eye
		
		if ttl == -1:
			self.ttl = round(random.gauss(2/3*Ant._MAX_TTL, Ant._MAX_TTL/4))
			if self.ttl < 0:
				self = 0
		else:
			self.ttl = ttl
			
		self.test()
		
	def test (self):
		assert self.will >= 0 and self.will <= Ant._MAX_WILL, "invalid will"
		assert self.eye >= 0 and self.eye <= Ant._MAX_EYESHOT, "invalid eye"
		assert self.ttl >= 0, "invalid ttl"
		
	# potomek vyuzivajici evoluci
	def child (self):
		# vůle
		will = round(random.gauss(self.will, Ant._MAX_WILL/6))
		if will < 0:
			will = 0
		elif will > Ant._MAX_WILL:
			will = Ant._MAX_WILL
		# dohled
		eye = round(random.gauss(self.eye, Ant._EYESHOT/6))
		if eye < 1:
			eye = 1
		elif eye > Ant._MAX_EYESHOT:
			eye = Ant._MAX_EYESHOT
		newAnt = Ant(will, eye)
		return newAnt
		
	
	def move (self, area, place):
		self.ttl -= 1
		if self.ttl < 0:	# ant dead
			return None
			
		assert place in AntHill.AntHill.places, "invalid place"
		
	def Print (self):
		print("-- Ant --")
		print("Will:", self.will)
		print("Range:", self.eye)
		print("Live:", self.ttl)
		
	

if __name__ == '__main__':
	ants = []
	for i in range(10):
		ant = Ant()
		ant.Print()
		ants.append(ant)
		
	print()
	area = []
	ants[0].move(area, "HOME")
# END