# By Pytel

from colr import color

DEBUG = True

class Place:
	
	_BASE_INTENZITY = 100
	_INTENZITY_DECAY = 2
	
	places = ["HOME", "FOOD", "DIRT", "STONE", "VOID"]
	
	def __init__ (self):
		self.content = []	# [[type, amount], ...]
		self.trace = []		# [[type, intenzity], ...]
		self.ants = []
		
	def isType (self, Typ):
		for content in self.content:
			typ, amount = content
			if typ == Typ:
				return True
		return False
		
	def takeFood (self):
		for content in self.content:
			typ, amount = content
			if typ == "FOOD":
				amount -= 1
				if amount == 0:
					self.content.remove(content)
					if DEBUG:
						print("jídlo vyčerpáno.")
				return True
		return False
		
	def intezityOf (self, Feromon):
		for feromon in self.trace:
			typ, intenzity = feromon
			if typ == Feromon:
				return intenzity
		return 0
		
	def addIntezity(self, feromon):
		for trace in self.trace:
			if trace[0] == feromon:
				trace[1] += Place._BASE_INTENZITY
				return
		self.trace.append([feromon, Place._BASE_INTENZITY])
		#print([feromon, Place._BASE_INTENZITY])
		
	def lowerIntezity(self):
		i = 0
		while i < len(self.trace):
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
		BR = 0; BG = 0; BB = 0
		if len(self.ants) != 0:
			char = 'A'
			brightnes = 40
			FR = brightnes*len(self.ants)
			FG = brightnes*len(self.ants)
			FB = brightnes*len(self.ants)
		
		for feromon in self.trace:
			typ, intenzity = feromon
			if typ == "HOME":
				BR += intenzity/10
			if typ == "FOOD":
				BG += intenzity/10
				
		for content in self.content:
			typ, amount = content
			if typ == "FOOD":
				char = 'F'
				brightnes = 25
				FG = brightnes*amount
			if typ == "HOME":
				char = 'H'
				brightnes = 255
				FR = brightnes*amount
				
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
				
# END