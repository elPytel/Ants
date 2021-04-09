# By Pytel

import random

DEBUG = True

class Ant:
	def __init__ (self, will = -1, eye = -1, ttl = -1):
		self._MAX_WILL = 100		# 0 - 100%
		self._MAX_EYESHOT = 3		# r - "radius"
		self._MAX_TTL = 1000		# time to live
		
		if will == 0:
			self.will = round(random.gauss(_MAX_WILL/2, _MAX_WILL/4))
		else:
			self.will = will
		
		if eye == -1:
			self.eye = round(random.gauss(1, _MAX_EYESHOT))
		else:
			self.eye = eye
		
		if ttl == -1:
			self.ttl = round(random.gauss(_MAX_TTL/2, _MAX_TTL/4))
		else:
			self.ttl = ttl
		
	# potomek vyuzivajici evoluci
	def child (self):
		# vůle
		will = round(random.gauss(self.will, self._MAX_WILL/6))
		if will < 0:
			will = 0
		elif will > self._MAX_WILL:
			will = self._MAX_WILL
		# dohled
		eye = round(random.gauss(self.eye, self._EYESHOT/6))
		if eye < 1:
			eye = 1
		elif eye > self._MAX_EYESHOT:
			eye = self._MAX_EYESHOT
		newAnt = Ant(will, eye)
		return newAnt
		
	
	def move (self, area, interest):
		self.ttl -= 1
		if self.ttl < 0:	# ant dead
			return None
			
		
	def Print (self):
		print(-- Ant --)
		print("Will:", self.will)
		print("Range:"), self.eye)
		print("Live:", self.ttl)

# END