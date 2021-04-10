# By Pytel

from colr import color

DEBUG = True

class Place:
	
	_BASE_INTENZITY = 100
	_INTENZITY_DECAY = 2
	_PLACES = ["HOME", "FOOD", "DIRT", "STONE", "VOID"]
	
	def __init__ (self):
		self.content = {}	# {[type, amount], ...}
		self.trace = {}		# {[type, intenzity], ...}
		self.ants = []
		
	def isType (self, typ):
		return True if typ in self.content.keys() else False
		
	def takeFood (self):
		amount = self.content.get("FOOD")
		if amount == None:
			return False
		amount -= 1
		if amount == 0:
			self.content.remove(content)
			if DEBUG:
				print("jídlo vyčerpáno.")
		return True
		
	def intezityOf (self, feromon):
		return self.trace[feromon] if feromon in self.trace.keys() else 0
		
	def addIntezity(self, feromon):
		intezity = self.trace.get(feromon)
		if intezity == None:
			self.trace[feromon] = Place._BASE_INTENZITY
		else:
			self.trace[feromon] = self.trace[feromon] + Place._BASE_INTENZITY
			#self.trace[feromon] += Place._BASE_INTENZITY
		
	def lowerIntezity(self):
		for feromon, intenzity in self.trace.items():
			if intenzity < Place._INTENZITY_DECAY:
				self.trace.pop(trace)
			else:
				intenzity -= Place._INTENZITY_DECAY
			self.trace[feromon] = intenzity
	
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
		
		for feromon, intenzity in self.trace.items():
			if feromon == "HOME":
				BR += intenzity/1	#10
			if feromon == "FOOD":
				BG += intenzity/1	#10
				
		for typ, amount in self.content.items():
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