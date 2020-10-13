from spot import *

class Board:
	def __init__ (self, x_width, y_length):
		self.x_width = x_width
		self.y_length = y_length
		self.spots = []
		for y in range(y_length):
			for x in range(x_width):
				self.spots.append(Spot(x, y, self))
		for spot in self.spots:
			spot.find_valid_spots(self.x_width, self.y_length, self)
		#print (self.spots)

	def get_spot(self, x, y):
		return (self.spots[(self.x_width* y) + x])
	
	def get_x_width(self):
		return self.x_width
	
	def get_y_length(self):
		return self.y_length
	
	def get_spot_index(self, other_spot):
		return self.spots.index(other_spot)
'''
	def get_spot_index(self, x, y):
		return (self.x_width * y) + x
'''
