from spot import *

class Board:
	def __init__ (self, x_width, y_width):
		self.x_width = x_width
		self.y_width = y_width
		self.spots = []
		for y in range(y_width):
			for x in range(x_width):
				self.spots.append(Spot(x, y, x_width, y_width))
		#print (self.spots)

	def get_spot(self, x, y):
		return (self.spots[(self.x_width* y) + x])
	
	def get_x_width(self):
		return self.x_width
	
	def get_y_width(self):
		return self.y_width
	
	def get_spot_index(self, other_spot):
		return self.spots.index(other_spot)
'''
	def get_spot_index(self, x, y):
		return (self.x_width * y) + x
'''
