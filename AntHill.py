# By Pytel

from colr import color
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
	
	def getColor (self):
		char = ' '
		FR = 0; FG = 0; FB = 0
		BG = 0; BG = 0; BB = 0
		if len(self.ants) != 0:
			char = 'A'
			brightnes = 20
			FR = brightnes*len(self.ants)
			FG = brightnes*len(self.ants)
			FB = brightnes*len(self.ants)
		
		for feromon in self.trace:
			typ, intenzity = feromon
			if typ == "HOME":
				BR += amount/10
			if typ == "FOOD":
				BG += amount/10
				
		for content in self.content:
			typ, amount = content
			if typ == "FOOD":
				char = 'F'
				
		# oriznuti barev na 255
		if BR > 255:
			BR = 255
		if BG > 255:
			BG = 255
			
		if FR > 255:
			FR = 255
		if FG > 255:
			FG = 255
		if FB > 255:
			FB = 255
			
		# navratovy format
		Fcolor = [FR,FG,FB]
		Bcolor = [BR,BG,BB]
		ret = [char, Fcolor, Bcolor]
		return ret
				

class AntHill:
	
	places = Place.places
	
	def __init__ (self, size, home, amount, terarium = None):
		self.Y, self.X = size
		if terarium == None:
			self.board = self.makeTerarium()
		else:
			self.board = terarium
		self.homeCoords	= home		# [y,x]
		y, x = self.homeCoords
		for i in range(amount):
			self.board[y][x].ants.append(Ants.Ant())
		
	def makeTerarium (self):
		terarium = []
		for y in range(self.Y):
			row = []
			for x in range(self.X): 
				row.append(Place())
			terarium.append(row)
			
		return terarium
		
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
						coord = ant.move(area)		# vektor posunu
						if coord == None:		# chcip mravenec
							place.ants.remove(ant)
							continue
						dy, dx = coord
						yn, xn = [y+dy,x+dx]		# nove souradnice
						assert self.validCoord([yn,xn]), "invalid coord"
						ant.moved = True
						place.ants.remove(ant)
						
						place_n = self.board[yn][xn].place
						place_n.ants.append(ant)
						place.addIntezity(ant.feromon)
		
	# vyhodnoti ubytek stop
	def evalDecay (self):
		for y in range(self.Y):
			for x in range(self.X):
				self.board[y][x].lowerIntezity()
			
	def Print (self):
		for row in self.board:
			for place in row:
				# [char, [R,G,B], [R,G,B]]
				char, Fc, Bc = place.getColor()	
				print(color(char, fore=(Fc[0], Fc[1], Fc[2]), back=(Bc[0], Bc[1], Bc[2])), end =" ")
			print()

if __name__ == '__main__':
	amount = 10
	size = [10, 10]
	# size, home, amount,
	hill = AntHill(size, [5,5], amount)
"""
 - Přepsat place na slovnik
pip install colr
"""				
# END