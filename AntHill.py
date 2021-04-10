# By Pytel

from colr import color
import copy
import time
import Ants
import Place

DEBUG = True

class AntHill:
	
	places = Place.Place._PLACES
	
	def __init__ (self, size, home, amount, terarium = None):
		self.Y, self.X = size
		if terarium == None:
			self.terarium = self.makeTerarium()
		else:
			self.terarium = terarium
		self.homeCoords	= home		# [y,x]
		y, x = self.homeCoords
		self.terarium[y][x].content["HOME"] = 1
		for i in range(amount):
			ant = Ants.Ant()
			#ant.feromon = "HOME"
			self.terarium[y][x].ants.append(ant)
		
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
		area = []
		ys, xs = coord
		for y in range(ys-r,ys+r+1):
			row = []
			for x in range(xs-r,xs+r+1):
				if self.validCoord([y,x]):
					row.append(copy.deepcopy(self.terarium[y][x]))
				else:
					place = Place.Place()
					place.content["VOID"] = 1
					row.append(place)
			area.append(row)
		return area
		
	def validCoord (self, coord):
		y, x = coord
		if y < 0 or y >= self.Y:
			return False
		if x < 0 or x >= self.X:
			return False
		return True
	
	def prepareAnts2Move (self):
		for y in range(self.Y):
			for x in range(self.X):
				place = self.terarium[y][x]
				for ant in place.ants:
					ant.moved = False
	
	def moveAnts (self):
		for y in range(self.Y):
			for x in range(self.X):
				place = self.terarium[y][x]
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
						
						place_n = self.terarium[yn][xn]
						place_n.ants.append(ant)
						place.addIntezity(ant.feromon)
		
	# vyhodnoti ubytek stop
	def evalDecay (self):
		for y in range(self.Y):
			for x in range(self.X):
				self.terarium[y][x].lowerIntezity()
			
	def Print (self):
		print("---Terarium---")
		for row in self.terarium:
			for place in row:
				# [char, [R,G,B], [R,G,B]]
				char, Fc, Bc = place.getColor()	
				print(color(char, fore=(Fc[0], Fc[1], Fc[2]), back=(Bc[0], Bc[1], Bc[2])), end ="")
			print()

if __name__ == '__main__':
	amount = 100
	size = [20, 60]
	# size, home, amount,
	hill = AntHill(size, [12,30], amount)
	hill.terarium[7][6].content["FOOD"] = 10
	hill.Print()
	for i in range(250):
		time.sleep(0.5)
		hill.prepareAnts2Move()
		hill.moveAnts()
		hill.evalDecay()
		hill.Print()
		
"""
 - Přepsat place na slovnik
 
	size = [10, 10]
	# size, home, amount,
	hill = AntHill(size, [5,5], amount)
	hill.board[2][2].content.append(["FOOD", 100])
	
pass

pip install colr
"""				
# END