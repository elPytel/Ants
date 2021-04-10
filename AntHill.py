# By Pytel

from colr import color
import time
import Ants
import Place

DEBUG = True

class AntHill:
	
	places = Place.Place.places
	
	def __init__ (self, size, home, amount, terarium = None):
		self.Y, self.X = size
		if terarium == None:
			self.board = self.makeTerarium()
		else:
			self.board = terarium
		self.homeCoords	= home		# [y,x]
		y, x = self.homeCoords
		self.board[y][x].content.append(["HOME", 1])
		for i in range(amount):
			ant = Ants.Ant()
			ant.feromon = "HOME"
			self.board[y][x].ants.append(ant)
		
	def makeTerarium (self):
		terarium = []
		for y in range(self.Y):
			row = []
			for x in range(self.X): 
				row.append(Place.Place())
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
					ant = place.ants[i]
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
						
						place_n = self.board[yn][xn]
						place_n.ants.append(ant)
						place.addIntezity(ant.feromon)
		
	# vyhodnoti ubytek stop
	def evalDecay (self):
		for y in range(self.Y):
			for x in range(self.X):
				self.board[y][x].lowerIntezity()
			
	def Print (self):
		print("---Terarium---")
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
	hill.board[2][2].content.append(["FOOD", 100])
	hill.Print()
	for i in range(10):
		time.sleep(1)
		hill.prepareAnts2Move()
		hill.moveAnts()
		hill.evalDecay()
		hill.Print()
		
"""
 - Přepsat place na slovnik
 
size = [15, 15]
	# size, home, amount,
	hill = AntHill(size, [10,10], amount)
	hill.board[5][5].content.append(["FOOD", 100])
	
pip install colr
"""				
# END