# By Pytel

import Ants

DEBUG = True

class Place:
	
	_BASE_INTENZITY = 100
	_INTENZITY_DECAY = 2
	
	places = ["HOME", "FOOD", "DIRT", "STONE", "VOID"]
	
	def __init__ (self):
		self.content = []	# [[type, amount], ...]
		self.trace = []		# [[type, intenzity], ...]
		self.ants = []
		
	def addIntezity(self, feromon):
		for trace in self.trace:
			if trace[0] == feromon:
				trace[1] += Place._BASE_INTENZITY
				return
		self.trace.append([feromon, Place._BASE_INTENZITY])
	
	def lowerIntezity(self):
		i = 0
		while i < len(place.trace):
			trace = self.trace[i]
			typ, intenzity = trace
			if intenzity < Place._INTENZITY_DECAY:
				self.trace.remove(trace)
			else:
				intenzity -= Place._INTENZITY_DECAY
				i += 1

class AntHill:
	
	places = Place.places
	
	def __init__ (self, amount, size = None):
		self.Y
		self.X
		self.board 
		self.homeCoords			# [y,x]
		y, x = self.homeCoords
		for i in range(amount):
			self.board[y][x].ants.append(Ant())
		
		
	# vrati sub matici
	def getArea (self, coord, r):
		# TODO
		pass
		
	def validCoord (self, coord):
		# TODO
		return True
	
	def prepareAnts2Move (self):
		for y in range(self.Y):
			for x in range(self.X):
				place = self.board[y][x]
				for ant in place.ants:
					ant.moved = False
	
	def moveAnts (self):
		for y in range(self.Y):
			for x in range(self.X):
				place = self.board[y][x]
				i = 0
				while i < len(place.ants):
					ant = place.ants(i)
					if ant.moved:
						i += 1
					else:
						area = self.getArea([y,x], ant.eye)
						dy, dx = ant.move(area)		# vektor posunu
						yn, xn = [y+dy,x+dx]		# nove souradnice
						assert self.validCoord(coord), "invalid coord"
						ant.moved = True
						self.board[y][x].place.ants.remove(ant)
						
						place_n = self.board[yn][xn].place
						place_n.ants.append(ant)
						place_n.addIntezity(ant.feromon)
		
	# vyhodnoti ubytek stop
	def evalDecay (self):
		for y in range(self.Y):
			for x in range(self.X):
				self.board[y][x].lowerIntezity()
				
						
# END