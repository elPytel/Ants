# By Pytel

import copy
import random
import AntHill

DEBUG = True

class Ant:
	
	_VECTORS = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
	_MAX_WILL = 100		# 0 - 100%
	_MAX_EYESHOT = 1	# r - "radius"
	_MAX_TTL = 1000		# time to live
		
	def __init__ (self, will = -1, eye = -1, ttl = -1):
		self.moved = True
		self.interest = None
		self.feromon = None
		self.carry = None
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
		
	
	def move (self, area):
		"""
		for row in area:
			for col in row:
				if col.isType("FOOD"):
					print('F', end ='')
				if col.isType("VOID"):
					print('V', end ='')
				else:
					print('_', end ='')
			print()
		"""
		vectors = copy.deepcopy(Ant._VECTORS)
		Y = self.eye
		X = self.eye
		
		self.ttl -= 1
		if self.ttl <= 0:	# ant dead
			return None
		
		# vyber feromon
		if area[Y][X].isType("HOME"):
			self.interest = "FOOD"
			self.feromon = "HOME"			
			self.carry = None
			if DEBUG:
				print("Našel jsem domov")
		elif area[Y][X].isType("FOOD"):			
			if area[Y][X].takeFood():
				self.interest = "HOME"
				self.feromon = "FOOD"
				self.carry = "FOOD"		# nese jidlo
				if DEBUG:
					print("Našel jsem jídlo")
					self.Print()
		
		# selekce
		i = 0
		while i < len(vectors):
			dy, dx = vectors[i]
			#print(Y+dy, X+dx)
			if area[Y+dy][X+dx].isType("VOID"):
				vectors.pop(i)
			else:
				i += 1
		
		# vidim co hledam?
		coord = None
		# minimax
		# [coord, feromon]
		coordInterest = []
		coordFeromon = []
		for y in range(len(area)):
			for x in range(len(area[0])):
				if y == Y and x == X or area[y][x].isType("VOID"):
					continue
				intezity = area[y][x].intezityOf(self.interest)
				coordInterest.append([[y, x], intezity])
				intezity = area[y][x].intezityOf(self.feromon)
				coordFeromon.append([[y, x], intezity])
				if area[y][x].isType(self.interest):
					coord = [y, x]
		
		# nasel co hledal
		if coord != None:
			dy = coord[0] - Y
			dx = coord[1] - X
			vector = [dy, dx]
			if DEBUG:
				print(coord)
			return vector	
		
		coordInterest.sort(key=lambda x: x[1], reverse=True)	# klesajici
		coordFeromon.sort(key=lambda x: x[1])					# rostouci
		
		
		# nic lepsiho nenalezeno
		return random.choice(vectors)	
		
		
	def Print (self):
		print("-- Ant --")
		print("Will:", self.will)
		print("Range:", self.eye)
		print("Live:", self.ttl)
		print("Interest:", self.interest)
		print("Feromon:", self.feromon)
		print("Carry:", self.carry)
		
	

if __name__ == '__main__':
	ants = []
	for i in range(10):
		ant = Ant()
		ant.Print()
		ants.append(ant)
		
	print()
	area = []
	ants[0].move(area)
	
"""
assert place in AntHill.AntHill.places, "invalid place"
"""
# END